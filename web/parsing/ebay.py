import re
from typing import List
from difflib import SequenceMatcher

from bs4 import BeautifulSoup
import requests
from concurrent.futures import as_completed, ThreadPoolExecutor
from parsing.models import Ebay, EbayAll


def get_page_item_urls(in_url) -> List[str]:
    # check some data before returning url, return only good items
    # return urls of items from listing
    soup = BeautifulSoup(requests.get(in_url).content.decode(), 'lxml')
    ebay_ = soup.find('div', class_="srp-river-results clearfix").find_all('li', class_="s-item s-item__pl-on-bottom s-item--watch-at-corner")
    ebay_items = []

    for ebay in ebay_:
        try:
            url = ebay.find('div', class_='s-item__wrapper clearfix').find('div', class_='s-item__info clearfix').find('a').get('href')
        except:
            url = ''

        ebay_items.append(url)
    return ebay_items


def get_page_detail(url) -> dict:
    soup = BeautifulSoup(requests.get(url).content.decode(), 'lxml')
    data = {'url': url}

    print(data['url'])

    try:
        title = soup.find('h1', id='itemTitle').text.strip('Details about')

    except:
        title = ''
    data['title'] = title
    # print(data['title'], 'title')
    # print(len(data['title']))

    try:
        condition = soup.find('div', id='vi-itm-cond').text

    except:
        condition = ''
    data['condition'] = condition
    # print(data['condition'], 'condition')

    try:
        quantity = soup.find('span', id='qtySubTxt').text.strip()
        n_quantity = re.findall(r'\b\d+\b', quantity)
        quantity = int(n_quantity[0]) if len(n_quantity) else 0

    except:
        quantity = 0
    data['quantity'] = quantity
    print(data['quantity'], 'quantity')

    try:
        star = soup.find('div', class_='ux-seller-section__content').text.strip('% Positive feedback').split()[2]
        # n_star = re.findall(r'\b\d+\b', star)
        # star = int(n_star[0]) if len(n_star) else 0
        star_n = int(star)
    except:
        star_n = 0
    data['star'] = star_n
    print(data['star'], 'star', type(star_n))

    try:
        percent = soup.find('div', class_='ux-seller-section__content').text.split()[4].strip('%')
        percent_n = float(percent)
    except:
        percent_n = 0
    data['percent'] = percent_n
    print(data['percent'], 'percent', type(percent_n))

    try:
        location = soup.find('span', itemprop='availableAtOrFrom').text.split()[-1]

    except:
        location = ''
    data['location'] = location
    # print(data['location'], 'location \n')

    return data


def ebay_main(instance):
    title = instance.title.replace(' ', '+')
    ebay_urls = [f'https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2380057.m570.l1313&_nkw={title}&_sacat=0', ]
    print(ebay_urls)
    items_data = []  # items from details page
    urls = []  # urls from listing page

    with ThreadPoolExecutor(max_workers=10) as executor:
        # todo: if many list pages with urls in them, use thread pool executor too to parse urls concurrently
        futures = {executor.submit(get_page_item_urls, url): url for url in ebay_urls}  # list urls -> 50 urls
        for future in as_completed(futures):
            url = futures[future]
            try:
                data = future.result()
                urls.extend(data)
                print(len(data))
            except Exception as exc:
                pass

        future_to_url = {executor.submit(get_page_detail, url): url for url in urls}
        for future in as_completed(future_to_url):
            url = future_to_url[future]
            try:
                data = future.result()
                items_data.append(data)
                # print('parsed item -> ', data)
            except Exception as exc:
                pass

    ## filtering and saving to database
    for item in items_data:
        similarity = round(SequenceMatcher(None, item['title'].lower(), instance.title.lower()).ratio() * 100)
        # print(similarity, '================== similarity allllllllllllll')

        if item['star'] < 100:
            continue
        elif item['condition'].lower() not in ['new', 'new with box']:
            continue
        elif item['percent'] < 98:
            continue
        elif item['location'].lower() not in ['states']:
            continue
        elif similarity < 1:
            continue
        ## saving parsed item to DB
        try:
            EbayAll.objects.update_or_create(url=item['url'], star=item['star'], quantity=item['quantity'],
                                             percent=item['percent'], product_title_id=instance.id, similarity=similarity,
                                            defaults={'title': item['title']})  # время 0.26358866691589355
        except Exception as e:
            print(e)


    for item in items_data:
        """ Filtering conditions:
        condition = new and new with box
        quantity = > 10
        star = > 100
        % = > 98%
        """
        """
        check title of parsed item title and imported title
        if ' '.join(item['title'].lower().split()[:4]) in ' '.join(instance.title.lower().split()[:4]):
            pass  # continue checking to save


        elif annotation[0] and annotation[0].lower() in item_titlee and \
                annotation[1] and annotation[1].lower() in item_titlee and \
                annotation[2] and annotation[2].lower() in item_titlee and \
                annotation[3] and annotation[3].lower() in item_titlee:
            pass
        """

        similarity = round(SequenceMatcher(None, item['title'].lower(), instance.title.lower()).ratio() * 100)
        print(similarity, '========== similarity (Ebay)')
        if item['star'] < 100:
            continue
        elif item['quantity'] < 3:
            continue
        elif item['condition'].lower() not in ['new', 'new with box']:
            continue
        elif item['percent'] < 98:
            continue
        elif item['location'].lower() not in ['states']:
            continue


        # # filtering by similar words
        # else:
        #     if instance.annotations:
        #         passing = True
        #         for i in ' '.join(instance.annotations.values()).split():
        #             print(i.lower().strip() in item['title'].lower(), '-------', item['title'].lower(), '-------', i.lower())
        #             if i.lower().strip() not in item['title'].lower():
        #                 passing = False
        #                 break
        #         if not passing:
        #             continue
        #     else:

        elif similarity < 70:
            continue
        # saving parsed item to DB
        try:
            Ebay.objects.update_or_create(url=item['url'], star=item['star'], quantity=item['quantity'],
                                          percent=item['percent'],  product_title_id=instance.id, similarity=similarity,
                                          defaults={'title': item['title']})   # время 0.26358866691589355
        except Exception as e:
            print(e)
    print(ebay_urls)

    return urls
