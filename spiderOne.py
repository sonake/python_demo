import requests as rs;
import os;
import time;
import threading;
from bs4 import BeautifulSoup;

def download_page(url):
    '''
    用于下载页面
    '''
    headers={
        "User-Agent":"Mozilla/5.0(Windows NT 10.0: Win64: x64: rv:61.0) Gecko/20100 Firefox/61.0"
    }
    r=rs.get(url,headers=headers);
    r.encoding='gb2312'
    return r.text;


def create_dir(param):
    if not os.path.exists(param):
        print(param)
        os.makedirs(param)


def get_pic(link, text):
    '''
    获取当前页面的图片，并保存
    :param link:
    :param text:
    :return:
    '''
    html=download_page(link) #下载界面
    soup=BeautifulSoup(html,'html.parser')
    #pic_list=soup.find('div',id="picture").find_all('img') #找到界面所有图片
    pic_list=soup.find('div',class_="thumb").find_all('img')
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0"}
    create_dir('pic/{}'.format(text))
    for i in pic_list:
        pic_link = i.get('src')  # 拿到图片的具体 url
        r = rs.get(pic_link, headers=headers)  # 下载图片，之后保存到文件
        with open('pic/{}/{}'.format(text, pic_link.split('/')[-1]), 'wb') as f:
            f.write(r.content)
            time.sleep(10)  # 休息一下，不要给网站太大压力，避免被封


def get_pic_list(html):
    '''
    获取每个页面的套图列表，之后循环调取get_pic函数获取图片
    :param html:
    :return:
    '''
    soup=BeautifulSoup(html,'html.parser')
    pic_list=soup.find_all('div',class_='thumb')
    for i in pic_list:
        a_tag=i.find('h3',class_='thumb').find('img')
        link=a_tag.get('href')
        text=a_tag.get_text();
        get_pic(link,text)
def execute(url):
    page_html = download_page(url)
    get_pic_list(page_html)


def main():
    create_dir('pic')
    queue = [i for i in range(1, 5)]   # 构造 url 链接 页码。
    threads = []
    while len(queue) > 0:
        for thread in threads:
            if not thread.is_alive():
                threads.remove(thread)
        while len(threads) < 5 and len(queue) > 0:   # 最大线程数设置为 5
            cur_page = queue.pop(0)
            # url = 'https://mzitu.org/a/more_{}.html'.format(cur_page)
            url = 'http://www.meizitu.org/fuli/963.html'
            print(url)
            thread = threading.Thread(target=execute, args=(url,))
            thread.setDaemon(True)
            thread.start()
            print('{}正在下载{}页'.format(threading.current_thread().name, cur_page))
            threads.append(thread)


if __name__ == '__main__':
    main()
        