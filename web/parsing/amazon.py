import time
import urllib
from random import randrange
from time import sleep
from typing import List
from difflib import SequenceMatcher
import requests
import socks
from bs4 import BeautifulSoup

import urllib.request as urllib2
from sockshandler import SocksiPyHandler

from concurrent.futures import as_completed, ThreadPoolExecutor

from parsing.models import Amazon

# header_list = [
#     'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
#     'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0',
#     'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_18_3) AppleWebKit/537.34 (KHTML, like Gecko) Chrome/82.0.412.92 Safari/539.36',
#     'Mozilla/5.0 (Macintosh; Intel Mac OS X 11.12; rv:87.0) Gecko/20170102 Firefox/78.0',
#     'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.32 (KHTML, like Gecko) Chrome/82.0.12.17 Safari/535.42'
# ]

headers = {
    'Host': 'www.amazon.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:70.0) Gecko/20100101 Firefox/70.0',
    # 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_18_3) AppleWebKit/537.34 (KHTML, like Gecko) Chrome/82.0.412.92 Safari/539.36',
    # 'User-Agent': 'Mozilla/5.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate, br',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
    'TE': 'Trailers'
}

# proxies = {
#     "http": "socks5://98.162.25.23"
# }
#

# proxies = {
#   # "http":'socks5://98.162.25.23',
#   # "https":'https://98.12.195.129'
#   # "http":'socks5://192.111.130.5'
#   # "https":'socks5://192.111.130.5'
#     "http": 'socks5://127.0.0.1:9050',
#     "https": 'socks5://127.0.0.1:9050'
#
# }

# opener = urllib2.build_opener(SocksiPyHandler(socks.SOCKS5, "127.0.0.1", 9050))

# print opener.open("http://www.somesite.com/") # All requests made by the opener will pass through the SOCKS proxy

# s = urllib2.build_opener(SocksiPyHandler(socks.SOCKS5, "127.0.0.1"))

s = requests.session()
proxies = {'http':  'socks5://167.179.75.165:33427'}

def get_page_item_urls(html) -> List[dict]:
    time.sleep(randrange(7))
    soup = BeautifulSoup(requests.get(html, proxies=proxies, headers=headers).content.decode(), 'html.parser')
        #request.urlopen(html).content.decode(), 'html.parser')
                         #
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
        amazons_url = [f"https://www.amazon.com/s?k={title}&ref=nb_sb_noss",]
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
                print(data)
            except Exception as exc:
                pass

    """ item_titlee = item['title'].lower()
        if instance.company and instance.company.lower() in item_titlee and \
             instance.unique_value and instance.unique_value.lower() in item_titlee and \
             instance.item_title and instance.item_title.lower() in item_titlee and \
             instance.volume and instance.volume.lower() in item_titlee:
        """

    for item in parsed_items:
        # if instance.annotations:
        #     passing = True
        #     for i in ' '.join(instance.annotations.values()).split():
        #         print(i.lower().strip() in item['title'].lower(), '-------', item['title'].lower(), '-------',
        #               i.lower())
        #         if i.lower().strip() not in item['title'].lower():
        #             passing = False
        #             break
        #     if not passing:
        #         continue
        # else:
            similarity = round(SequenceMatcher(None, item['title'].lower(), instance.title.lower()).ratio() * 100)
            print(similarity, '================== similarity')
            if similarity < 75:
                continue

            try:
                Amazon.objects.update_or_create(url=item['url'], product_title_id=instance.id,
                                                defaults={'title': item['title']})
            except Exception as e:
                print(e)

    return parsed_items







