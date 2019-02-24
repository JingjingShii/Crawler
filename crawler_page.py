from bs4 import BeautifulSoup
from selenium import webdriver
import time
import urllib.request


def get_request(url):

    driver = webdriver.PhantomJS(executable_path='/Users/Jingjing/PycharmProjects/crawler/phantomjs-2.1.1-macosx/bin/phantomjs')
    # driver = webdriver.Chrome('/Users/Jingjing/PycharmProjects/crawler/chromedriver')
    driver.get(url)
    time.sleep(10)
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

G = None


def get_image(text):
    global G
    if G is None:
        G = 1

    img_htmls = text.find_all('div', class_ = 'files__file__preview')
    for img_html in img_htmls:
        img_url = img_html.find('div')['style']
        new_img_url = img_url[22:-2]

        print(new_img_url)

        urllib.request.urlretrieve(new_img_url, '/Users/Jingjing/PycharmProjects/crawler/' + str(G) +'.png')

        G = G + 1


def load_more_page(text):

    text.find_element_by_xpath('//*[@class="btn btn--blue"]').click()
    time.sleep(10)
    content = text.page_source
    soup = BeautifulSoup(content, 'lxml')

    return soup


P = None


def get_code_page(url):

    global P
    if P is None:
        P = 1

    driver = get_request(url)
    driver.find_element_by_xpath('//*[@class="share-file__navigation__item"][2]').click()
    time.sleep(10)

    driver.find_element_by_xpath('//*[@class="Select-arrow"]').click()

    # driver.find_element_by_xpath('//div[@class="Select-input"][@aria-activedescendant="react-select-6--option-1"]').click()

    # driver.find_element_by_xpath('//*[@id="react-select-6--vale"]/div[2][@aria-activedescendant="react-select-6--option-1"]').click()

    driver.find_element_by_xpath('//div[contains(@id, "option-1")]').click()

    time.sleep(10)
    # driver.save_screenshot('/Users/Jingjing/PycharmProjects/crawler/douban.png')

    content = driver.page_source
    soup = BeautifulSoup(content, 'lxml')

    a = soup.find('pre', class_ = "shareplot__content__code__content").text

    name = str(P) +'.py'

    with open(name, 'a+', encoding = 'utf-8') as f:
        f.write(a)

    P = P + 1


def main():

    url = 'https://plot.ly/feed/?q=filetype:plot'
    driver = get_request(url)

    # for i in range(4):
    #
    #     test_load = load_more_page(driver)
    #
    # get_image(test_load)

    test_load = load_more_page(driver)

    items = get_page(test_load)

    new_page_url = []

    for i in items:
        new_url = i + '#code'
        new_page_url.append(new_url)

    print(new_page_url)

    for i in new_page_url:
        get_code_page(i)





if __name__ == '__main__':
    main()
