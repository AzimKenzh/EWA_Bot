from random import randrange
from time import sleep
from typing import List
from difflib import  SequenceMatcher

import requests
from bs4 import BeautifulSoup

from concurrent.futures import as_completed, ThreadPoolExecutor

from parsing.models import Amazon

headers = {
    'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.1.1 Safari/605.1.15",
    'Accept-Language': "en-gb",
    'Accept-Encoding': 'br, gzip, deflate',
    'Accept': 'test/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Referer': 'https://www.google.com/'
}


def get_page_item_urls(html) -> List[dict]:
    sleep(randrange(7))
    soup = BeautifulSoup(requests.get(html, headers=headers).content.decode(), 'lxml')
    print(soup)
    amazon_ = soup.find_all('div',
                            class_='sg-col-4-of-12 s-result-item s-asin sg-col-4-of-16 sg-col s-widget-spacing-small sg-col-4-of-20')

    amazon_items = []

    for amazon in amazon_:
        title = amazon.find('span', class_='a-size-base-plus a-color-base a-text-normal').text
        try:
            url = f"https://www.amazon.com{amazon.find('h2', class_='a-size-mini a-spacing-none a-color-base s-line-clamp-4').find('a').get('href')}"
        except:
            url = ''

        data = {'url': url, 'title': title}
        amazon_items.append(data)
    return amazon_items


def amazon_main(instance=None):
    if instance:
        title = instance.title.replace(' ', '+')
        amazons_url = [f'https://www.amazon.com/s?k={title}&ref=nb_sb_noss',]
    else:
        ''

    parsed_items = []

    with ThreadPoolExecutor(max_workers=10) as executor:
        futures = {executor.submit(get_page_item_urls, url): url for url in amazons_url}
        for future in as_completed(futures):
            url = futures[future]
            try:
                data = future.result()
                parsed_items.extend(data)
            except Exception as exc:
                pass

    for item in parsed_items:

        item_titlee = round(SequenceMatcher(None, item['title'].lower(), instance.title).ratio() * 100)
        print(item_titlee, '------site------', item['title'], '--------import------', instance.title)
        # item_titlee = item['title'].lower()
        # if instance.company and instance.company.lower() in item_titlee and \
        #      instance.unique_value and instance.unique_value.lower() in item_titlee and \
        #      instance.item_title and instance.item_title.lower() in item_titlee and \
        #      instance.volume and instance.volume.lower() in item_titlee:
        #     try:
        #         Amazon.objects.update_or_create(url=item['url'], product_title_id=instance.id,
        #                                         defaults={'title': item['title']})
        #     except Exception as e:
        #         print(e)

    return parsed_items







