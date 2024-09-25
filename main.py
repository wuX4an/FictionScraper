# FictioScraper <Make by wuX4an>
import requests
from bs4 import BeautifulSoup

def response(url:str):
    cookies = {
        'csrftokenfe': 'YourFictionExpressToken',
        'cookie_fiction_express': 'true',
        'fictionexpressid': 'YourFictionExpressID',
    }

    headers = {
        'User-Agent': 'FictionScraper',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/png,image/svg+xml,*/*;q=0.8',
        'Accept-Language': 'es-MX,es;q=0.8,en-US;q=0.5,en;q=0.3',
    }

    return requests.get(url, cookies=cookies, headers=headers)

def extract(response):
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        content = soup.find('div', id="texto")

        if content:
            paragraphs = []
            for paragraph in content.find_all('p'):
                for span in paragraph.find_all('span'):
                    span.replace_with(span.text)
                paragraphs.append(paragraph.text)
            return  ' '.join(paragraphs)
        else:
            return []

def pages_num(pages:int, url:str):
  urls = []
  for i in range(1, pages + 1):
    urls.append(url + str(i))
  return urls


# Tests:
# print(pages_num(11, 'https://lat.fictionexpress.com/libros/armonia/capitulos/2-el-jardin-y-el-gallinero/'))
# print(extract(response('https://lat.fictionexpress.com/libros/armonia/capitulos/2-el-jardin-y-el-gallinero/1/')))


pages = 11
url = 'https://lat.fictionexpress.com/libros/armonia/capitulos/2-el-jardin-y-el-gallinero/'



for i in pages_num(pages, url):
  print(extract(response(i)))

# NOTE: Cheating is wrong.
