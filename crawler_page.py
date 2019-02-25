from bs4 import BeautifulSoup
from selenium import webdriver
import time
import urllib.request
from concurrent.futures import ProcessPoolExecutor,as_completed


def get_request(url):

    driver = webdriver.PhantomJS(executable_path='/Users/Jingjing/PycharmProjects/crawler/phantomjs-2.1.1-macosx/bin/phantomjs')
    # driver = webdriver.Chrome('/Users/Jingjing/PycharmProjects/crawler/chromedriver')

    driver.get(url)

    time.sleep(15)

    return driver


def get_page(driver):
    # html = driver.page_source
    # soup = BeautifulSoup(driver, 'lxml')
    items = driver.find_all('div', class_ = 'files__file files__file--plot files__file--thumbnail files__file--view')
    # get_image(soup)

    pages = []

    for item in items:

        url = item.find('a', class_ = 'files__file__open-btn btn', text = 'View').get('href')

        url_new = 'https://plot.ly'+url

        pages.append(url_new)

    print(pages)

    return pages

def get_image(text):

    img_htmls = text.find_all('div', class_ = 'files__file__preview')

    items = text.find_all('div', class_='files__file files__file--plot files__file--thumbnail files__file--view')

    pages = []

    for item in items:

        url = item.find('a', class_ = 'files__file__open-btn btn', text = 'View').get('href')

        url_new = 'https://plot.ly'+url

        pages.append(url_new)

    i = 0

    for img_html in img_htmls:

        img_url = img_html.find('div')['style']
        new_img_url = img_url[22:-2]

        print(new_img_url)

        name = pages[i].replace('/','')

        print(name)

        urllib.request.urlretrieve(new_img_url, '/Users/Jingjing/PycharmProjects/crawler/' + name+'.png')

        i = i + 1



def load_more_page(text):

    text.find_element_by_xpath('//*[@class="btn btn--blue"]').click()
    time.sleep(10)
    content = text.page_source
    soup = BeautifulSoup(content, 'lxml')

    return soup


def get_code_page(url):

    driver = get_request(url)
    # driver.find_element_by_xpath('//*[@class="share-file__navigation__item"][2]').click()

    driver.find_element_by_xpath('//*[@id = "app-content__with-header"]/div/div/div[2]/a[3]').click()

    time.sleep(10)

    driver.find_element_by_xpath('//*[@class="Select-arrow"]').click()

    driver.find_element_by_xpath('//div[contains(@id, "option-1")]').click()

    time.sleep(10)
    # driver.save_screenshot('/Users/Jingjing/PycharmProjects/crawler/douban.png')

    content = driver.page_source
    soup = BeautifulSoup(content, 'lxml')

    a = soup.find('pre', class_ = "shareplot__content__code__content").text

    name = url.replace('/','')
    name = name + '.py'

    with open(name, 'a+', encoding = 'utf-8') as f:
        f.write(a)


def main():

    url = 'https://plot.ly/feed/?q=filetype:plot'
    driver = get_request(url)

    for i in range(1):

        test_load = load_more_page(driver)

    # get_image(test_load)

    items = get_page(test_load)

    new_page_url = []

    for i in items:
        new_url = i + '#code'
        new_page_url.append(new_url)

    print(new_page_url)


    with ProcessPoolExecutor(4) as pool:
        pool.map(get_code_page, new_page_url)





if __name__ == '__main__':
    main()

