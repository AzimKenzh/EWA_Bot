import re

from bs4 import BeautifulSoup
import requests

from parsing.models import Ebay


def get_page_item_urls(html):
    # return urls of items from listing
    soup = BeautifulSoup(html, 'lxml')
    ebay_ = soup.find('div', class_="srp-river-results clearfix").find_all('li', class_="s-item s-item__pl-on-bottom")
    ebay_items = []

    for ebay in ebay_:
        try:
            url = ebay.find('div', class_='s-item__info clearfix').find('a').get('href')
        except:
            url = ''

        ebay_items.append(url)

    return ebay_items


def get_page_detail(url):
    soup = BeautifulSoup(requests.get(url).content.decode(), 'lxml')
    data = {'url': url}

    try:
        title = soup.find('h1', id='itemTitle').text

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

    return data


def main(index_url):
    # 50 listing, 20 items in each maybe
    html = requests.get(index_url).content.decode()
    urls = get_page_item_urls(html)

    items_data = []  # items from details page
    for url in urls:
        items_data.append(get_page_detail(url))
    print(items_data)

    # filtering and saving to database
    for item in items_data:
        """ Filtering conditions:
        condition = new and new with box
        quantity = > 10
        star = > 100
        % = > 98%
        """
        if item['star'] < 100:
            continue
        elif item['quantity'] < 10:
            continue
        elif item['condition'].lower() not in ['new', 'new with box']:
            continue
        elif item['percent'] < 98:
            continue
        Ebay.objects.update_or_create(url=item['url'], defaults={'title': item['title']})


if __name__ == '__main__':
    EBAY_URL = 'https://www.ebay.com/sch/i.html?_from=R40&_nkw=maybelline+instant+age+rewind+eraser+dark+circles+treatment+multi-use+concealer+light++0.2+oz&_sacat=0&LH_TitleDesc=0&_fcid=1&_sop=10&LH_ItemCondition=3&_fsrp=1&LH_PrefLoc=1&LH_All=1&rt=nc&_oaa=1&_dcat=11865'
    main(EBAY_URL)
