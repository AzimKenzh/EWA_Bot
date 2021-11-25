from bs4 import BeautifulSoup
import requests


headers = {
    'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.1.1 Safari/605.1.15",
    'Accept-Language': "en-gb",
    'Accept-Encoding': 'br, gzip, deflate',
    'Accept': 'test/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Referer': 'https://www.google.com/'
}

#
# def get_all_page_urls(html):
#     print(url)
#     all_urls = set()
#     soup = BeautifulSoup(html, 'lxml')
#     nav_elem = soup.find('nav', class_="mt6 mb5")
#     print(nav_elem, 'testtttttttttttttttttttttttttt')
#     pages_ul = nav_elem.find('ul') if nav_elem else []
#     page_elems = pages_ul.find_all('li')
#     for i in page_elems:
#         all_urls.update(i.find('a').get('href'))
#
#     return list(all_urls)


def get_page_item_urls_w(html):
    soup = BeautifulSoup(html, 'lxml')
    walmart_ = soup.find_all('div', class_='mb1 ph1 pa0-xl bb b--near-white w-25')
    url_items = []
    # for i in walmart_:
    #     url_items.append(i.find_all('a', class_='absolute w-100 h-100 z-1'))
    # urls = []
    # for i in url_items:
    #     for j in i:
    #         url = j.get('href')
    #         url = f'https://www.walmart.com{url}' if not url.startswith('https://www.walmart.com') else url
    #         urls.append(url)
        # urls.append(url_items)

    for walmart in walmart_:
        title = walmart.find('span', class_='w_Bj').find('span', class_='f6 f5-l normal dark-gray mb0 mt1 lh-title').text
        url = f"https://www.walmart.com{walmart.find('a', class_='absolute w-100 h-100 z-1').get('href')}"
        quantity = walmart.find('div', class_='absolute z-2 bottom--1').find('span').text
        # quantity_2 = walmart.find('div', class_='flex flex-row justify-between pa1 br-pill f5 sans-serif').get('span')
        data = {'title': title, 'url': url, 'quantity': quantity} #, 'quantity_2': quantity_2}
        url_items.append(data)
    return url_items


def walmart_main():
    url = 'https://www.walmart.com/search?q=Maybelline+Instant+Age+Rewind+Eraser+Dark+Circles+Treatment+Concealer++Warm+Light+0.2+++Oz+'
    page_urls = [url + f'&page={x}' for x in range(2, 4)]
    page_urls.append(url)
    # page_urls = get_all_page_urls(requests.get(url, headers=headers).content.decode())
    url_items = []
    for i in page_urls:
        html = requests.get(i, headers=headers).content.decode()
        items = get_page_item_urls_w(html)
        url_items.extend(items)

    return url_items
