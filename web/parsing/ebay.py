import re
from typing import List

from bs4 import BeautifulSoup
import requests
from concurrent.futures import as_completed, ThreadPoolExecutor
from parsing.models import Ebay


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

    try:
        title = soup.find('h1', id='itemTitle').text.strip('Details about')
        # print(title.lower())

    except:
        title = ''
    data['title'] = title

    try:
        condition = soup.find('div', id='vi-itm-cond').text

    except:
        condition = ''
    data['condition'] = condition

    try:
        quantity = soup.find('span', id='qtySubTxt').text.strip()
        n_quantity = re.findall(r'\b\d+\b', quantity)
        quantity = int(n_quantity[0]) if len(n_quantity) else 0

    except:
        quantity = 0
    data['quantity'] = quantity

    try:
        star = soup.find('span', class_='mbg-l').find('a').text
        n_star = re.findall(r'\b\d+\b', star)
        star = int(n_star[0]) if len(n_star) else 0
    except:
        star = 0
    data['star'] = star

    try:
        percent = soup.find('div', id='si-fb').text
        n_percent = re.findall(r'\b\d+\b', percent)
        percent = int(n_percent[0]) if len(n_percent) else 0

    except:
        percent = 0
    data['percent'] = percent


    try:
        location = soup.find('span', itemprop='availableAtOrFrom').text.split()[-1]

    except:
        location = ''
    data['location'] = location

    return data


def ebay_main(instance):
    title = instance.title.replace(' ', '+')
    ebay_urls = [f'https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2380057.m570.l1313&_nkw={title}&_sacat=0', ]

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
                # print('parsed listing urls -> ', len(data), data)
            except Exception as exc:
                pass
                # print('%r generated an exception: %s' % (data, exc))

        future_to_url = {executor.submit(get_page_detail, url): url for url in urls}
        for future in as_completed(future_to_url):
            url = future_to_url[future]
            try:
                data = future.result()
                items_data.append(data)
                # print('parsed item -> ', data)
            except Exception as exc:
                pass
                # print('%r generated an exception: %s' % (data, exc))

        # print(len(items_data), '-------------------------------------------------')

    # # filtering and saving to database
    for item in items_data:
        """ Filtering conditions:
        condition = new and new with box
        quantity = > 10
        star = > 100
        % = > 98%
        """
        # print(item['title'], REDUCTION_TITLE)
        # check title of parsed item title and imported title
        if ' '.join(item['title'].lower().split()[:4]) in ' '.join(instance.title.lower().split()[:4]):
            pass  # continue checking to save
        elif item['star'] < 100:
            continue
        elif item['quantity'] < 3:
            continue
        elif item['condition'].lower() not in ['new', 'new with box']:
            continue
        elif item['percent'] < 98:
            continue
        elif item['location'].lower() not in ['states']:
            continue
        # saving parsed item to DB
        try:
            Ebay.objects.update_or_create(url=item['url'], star=item['star'], quantity=item['quantity'],
                                          percent=item['percent'],  product_title_id=instance.id,
                                          defaults={'title': item['title']})   # время 0.26358866691589355
        except Exception as e:
            print(e)
        # print(len(urls))
    return urls
