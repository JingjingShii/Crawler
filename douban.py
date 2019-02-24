import requests
from bs4 import BeautifulSoup
import json

def start_requests(url):
    print(url)
    r = requests.get(url)
    return r.content

def get_page(text):
    soup = BeautifulSoup(text, 'html.parser')
    movies = soup.find_all('div', class_ = 'info')
    pages = []
    for moive in movies:
        url = moive.find('div', class_ = 'hd').a['href']
        pages.append(url)

    return pages

def pars_pages(text):

    soup = BeautifulSoup(text,'html.parser' )
    mydict = {}
    mydict['title'] = soup.find('span', property = 'v:itemreviewed').text
    mydict['duration'] = soup.find('span', property = 'v:runtime').text
    mydict['time'] = soup.find('span', property='v:initialReleaseDate').text

    return mydict

def write_json(result):
    s = json.dumps(result, indent = 4, ensure_ascii=False)
    with open('movies.json', 'w', encoding = 'utf-8') as f:
        f.write(s)

def main():
    for i in range(7, 9):
        url = 'https://movie.douban.com/top250?start={}&filter='.format(i * 25)
        text = start_requests(url)
        pageurls = get_page(text) # 解析一级页面
        for pageurl in pageurls: # 解析二级页面
            page = start_requests(pageurl)
            mydict = pars_pages(page)
            result_list.append(mydict)
    write_json(result_list) # 所有电影都存进去之后一起输出到文件

if __name__ == '__main__':
    result_list = []
    main()

