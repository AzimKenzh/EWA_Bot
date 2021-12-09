# from pprint import pprint
# from typing import List
#
# from bs4 import BeautifulSoup
# import requests
# from concurrent.futures import as_completed, ThreadPoolExecutor
#
#
# headers = {
#     'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.1.1 Safari/605.1.15",
#     'Accept-Language': "en-us",
#     'Accept-Encoding': 'br, gzip, deflate',
#     'Accept': 'test/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#     'Referer': 'https://www.google.com/'
# }
#
#
# def get_page_item_urls(in_url) -> List[str]:
#     soup = BeautifulSoup(requests.get(in_url, headers=headers).content.decode(), 'lxml')
#     walmart_ = soup.find_all('div', class_='mb1 ph1 pa0-xl bb b--near-white w-25')
#     url_items = []
#
#     for walmart in walmart_:
#         # title = soup.find('span', class_='f6 f5-l normal dark-gray mb0 mt1 lh-title').text
#         url = f"https://www.walmart.com{walmart.find('a', class_='absolute w-100 h-100 z-1').get('href')}"
#         # quantity = soup.find('div', class_='absolute z-2 bottom--1').find('span').text
#         # shipping = soup.find('span', class_='w_A w_C w_B mr1 mt1 ph1').text
#         # # quantity_2 = walmart.find('div', class_='flex flex-row justify-between pa1 br-pill f5 sans-serif').get('span')
#         # data = {'title': title, 'url': url, 'quantity': quantity, 'shipping': shipping} #,quantity_2 '': quantity_2}
#         url_items.append(url)
#     return url_items
#
#
# def get_page_detail(url) -> dict:
#     soup = BeautifulSoup(requests.get(url, headers=headers).content.decode(), 'lxml')
#     print(soup)
#     data = {'url': url}
#
#     title = soup.find('h1', itemprop='name').text
#     # if title:
#     #     title = title.text.strip()
#     data['title'] = title or ''
#
#     time = soup.find('span', class_='b black').text
#     # if time:
#     #     time = time.text.replace('arrives by').strip()
#     data['time'] = time or ''
#
#     pprint(data)
#     return data
#
#
# def walmart_main():
#     list_urls = ['https://www.walmart.com/search?q=Maybelline+Instant+Age+Rewind+Eraser+Dark+Circles+Treatment+Concealer++Warm+Light+0.2+Oz']
#
#     # page_urls = [list_urls + f'&page={list(x)}' for x in range(2, 4)]
#     # page_urls.append(list_urls)
#     # # page_urls = get_all_page_urls(requests.get(url, headers=headers).content.decode())
#     # url_items = []
#     # for i in page_urls:
#     #     in_url = requests.get(i, headers=headers).content.decode()
#     #     items = get_page_item_urls(in_url)
#     #     url_items.extend(items)
#
#     items_data = []
#
#     urls = []
#
#     with ThreadPoolExecutor(max_workers=10) as executor:
#         # todo: if many list pages with urls in them, use thread pool executor too to parse urls concurrently
#         futures = {executor.submit(get_page_item_urls, url): url for url in list_urls}  # list urls -> 50 urls
#         for future in as_completed(futures):
#             url = futures[future]
#             try:
#                 data = future.result()
#                 urls.extend(data)
#                 print('parsed listing urls -> ', len(data), data)
#             except Exception as exc:
#                 print('%r generated an exception: %s' % (data, exc))
#
#         future_to_url = {executor.submit(get_page_detail, url): url for url in urls}
#         for future in as_completed(future_to_url):
#             url = future_to_url[future]
#             try:
#                 data = future.result()
#                 items_data.append(data)
#                 print('parsed item -> ',  data)
#             except Exception as exc:
#                 print('%r generated an exception: %s' % (data, exc))
#
#     return items_data
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# # """SELENIUM"""
# # import csv
# #
# # from selenium import webdriver
# #
# # # from seleniumrequests import Chrome
# #
# #
# # headers = {
# #     'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.1.1 Safari/605.1.15",
# #     'Accept-Language': "en-gb",
# #     'Accept-Encoding': 'br, gzip, deflate',
# #     'Accept': 'test/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
# #     'Referer': 'https://www.google.com/'
# # }
# #
# #
# # def walmart_main():
# #     driver = webdriver.Chrome()
# #     driver.get("https://www.walmart.com/search?q=Maybelline+Instant+Age+Rewind+Eraser+Dark+Circles+Treatment+Concealer++Warm+Light+0.2+++Oz")
# #     # url = "https://www.walmart.com/search?q=Maybelline+Instant+Age+Rewind+Eraser+Dark+Circles+Treatment+Concealer++Warm+Light+0.2+++Oz"
# #     # response = driver.request(headers=headers, url=url)
# #     elem = driver.find_element_by_class_name("f6 f5-l normal dark-gray mb0 mt1 lh-title")
# #     print(elem.text)
# #
# #
# # if __name__ == "__main__":
# #     walmart_main()
#
#
