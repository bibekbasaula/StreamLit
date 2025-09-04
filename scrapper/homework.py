import requests
from bs4 import BeautifulSoup
import csv


books = []
dic = {}
url = 'https://books.toscrape.com/'


def books_scrapper(url):

    response = requests.get(url)
    print(response.status_code)
    if response.status_code != 200:
        print('Failed to fetch data')
        return []
    
    soup = BeautifulSoup(response.text, 'html.parser')
    articles = soup.find_all('article', class_='product_pod')

    for article in articles:
        title = article.h3.a['title']
        price_raw = soup.find('p', class_='price_color').text
        price = price_raw.encode('latin-1').decode('utf-8')

        dic = {
            'title':title,
            'currency':price[0],
            'amount':price[1:],
        }

        books.append(dic)


    return books

all_books = books_scrapper(url)

with open('data.csv','w', newline='') as f:
    writer = csv.DictWriter(f , fieldnames=all_books[0].keys())
    writer.writeheader()
    writer.writerows(books)




    
    


