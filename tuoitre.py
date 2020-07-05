from urllib.parse import urljoin
import requests
import bs4


BASE_URL = 'https://tuoitre.vn'
SOURCE_URL = 'https://tuoitre.vn/tin-moi-nhat.htm'

def get_article_content(url):
    data = {}
    r = requests.get(url)
    if r.ok:
        s = bs4.BeautifulSoup(r.content,"lxml")
        title = s.select_one('h1.article-title')   
        data['title'] = title.text.strip()
        
        sub_title = s.select_one('#mainContentDetail > div.column-first-second > div.main-content-body > h2')
        data['sub_title'] = sub_title.text.strip() if sub_title else ''

        content = s.select_one('#main-detail-body')
        data['content'] = content.prettify() if content else ''
    return data


def main():
    r = requests.get(SOURCE_URL)
    if r.ok:
        s = bs4.BeautifulSoup(r.content,"lxml")
        links = s.select('h1.article-title')
        for a in links:
            print('url:', urljoin(BASE_URL, a.attrs['href']))
    else:
        print('khong truy cap duoc')

if __name__=='__main__':
    # main()
    print(get_article_content('https://tuoitre.vn/do-phong-toa-dan-anh-ra-quan-nhau-nhu-phat-ro-20200705215453896.htm'));
    