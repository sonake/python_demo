from bs4 import BeautifulSoup
import requests
import os


#   URL="http://www.nationalgeographic.com.cn/animals/"
start=input("请输入起始页:")
end=input("请输入结束页:")
def download():
    p=int(start);q=int(end);
    while q >= p:
        s="/page/"+str(p)+"/";
        URL = "http://www.meizitu.org"+s;
        p += 1;
        html = requests.get(URL).text
        soup = BeautifulSoup(html, 'html.parser')
        # img_url=soup.find_all('div',{'class':"img_list"})
        img_url = soup.find_all('div', {'class': "thumb"})
        # os.makedirs('./img/', exist_ok=True)
        os.makedirs('./mzitu2/', exist_ok=True)
        for ul in img_url:
            imgs = ul.find_all('img')
            for img in imgs:
                url = img['src']
                r = requests.get(url, stream=True)
                img_name = url.split('/')[-1]
                with open('./mzitu2/%s' % img_name, 'wb')as f:
                    for chunk in r.iter_content(chunk_size=128):
                        f.write(chunk)
                print('Saved %s' % img_name)


download()
