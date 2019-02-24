import requests
from bs4 import BeautifulSoup
import json
import re
from selenium import webdriver
import time


# def getHTMLText(url):
#     driver = webdriver.PhantomJS(executable_path='/Users/Jingjing/PycharmProjects/crawler/phantomjs-2.1.1-macosx/bin/phantomjs')  # phantomjs的绝对路径
#     time.sleep(2)
#     driver.get(url)  # 获取网页
#     time.sleep(2)
#     return driver.page_source


# def start_requests(url):
#     print(url)
#     r = requests.get(url, timeout = 10)
#     return r.content


def get_page(text):
    soup = BeautifulSoup(text, 'html.parser')
    items = soup.find_all('div', class_ = 'files_file_footer')
    print(items)
    pages = []
    for item in items:
        url = item.find_all('div', class_ = 'files_file_buttons').a['href']
        pages.append(url)

    return pages

def main():

    url = 'https://plot.ly/feed/?q=filetype:plot'
    text = getHTMLText(url)
    pageurls = get_page(text) # 解析一级页面
    print(pageurls)

if __name__ == '__main__':
    result_list = []
    main()
