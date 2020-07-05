import requests
import bs4

SOURCE_URL = 'https://tuoitre.vn/tin-moi-nhat.htm'

def main():
    r = requests.get(SOURCE_URL)
    if r.ok:
        s = bs4.BeautifulSoup(r.content,"lxml")
        links = s.select('div.name-news > h3 > a')
        for a in links:
            print(a.attrs['href'])
    else:
        print('khong truy cap duoc')

if __name__=='__main__':
    main()

    #content > div > div.list-middle > div > div.w664.fl.stream-home.list-middle-content > div > ul > li:nth-child(1) > div.name-news > h3 > a