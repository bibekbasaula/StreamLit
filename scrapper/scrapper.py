import requests
import json
from bs4 import BeautifulSoup
dic = {}
books = []
url = 'https://books.toscrape.com/'


def scrape_books(url):
    response = requests.get(url)
    # print(response.status_code)
    if response.status_code != 200:
        print('Cannot fetch data')
        return

    response.encoding = response.apparent_encoding

    # print(response.text)
    soup = BeautifulSoup(response.text, 'html.parser')
    articles = soup.find_all("article", class_='product_pod')
    # print(articles)
    for article in articles:
        title = article.h3.a['title']
        priceText = article.find('p', class_='price_color').text
        # print(title)
        # print(priceText[0])
        # print(float(priceText[1:]))
        dic = {
            'title': title,
            'currency': priceText[0],
            'amount': float(priceText[1:])
        }
        books.append(dic)

    return books



    

all_books = scrape_books(url)

with open('books.json','w', encoding= 'utf-8') as f:
    json.dump(all_books , f, indent=2, ensure_ascii=False)

