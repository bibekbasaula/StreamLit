# python -m pip install requests
# => get data from web (html , json, xml)

#python -m pip install beautifulsoup4
# => parse html

#go to git bash
# git config --global user.name 'Bibek Basaula'
# git config --global user.email 'radhikabasaula12@gmail.com'

# git init
# git status -> if you want to check what are the status of files
# git diff -> if you want to check what are the changes
# git add .
# git commit -m "Your message"
# copy paste git code from github

##########################################
### 1. Change the code                 ###
### 2. git add .                       ###
### 3. git commit -m 'Your message"    ###
### 4. git push                        ###
##########################################






import csv
import json
import requests
from bs4 import BeautifulSoup
dic = {}
books = []


url = 'https://books.toscrape.com/'

def books_scrapper(url):

    response = requests.get(url)
    if response.status_code != 200:
        print('Data not fetchable')
        return []
    
    soup = BeautifulSoup(response.text , 'html.parser' )
    articles = soup.find_all('article', class_='product_pod')

    for article in articles:
        title = article.h3.a['title']
        price_raw = article.find('p', class_='price_color').text
        price = price_raw.encode('latin-1').decode('utf-8')
        available = article.find('p', class_='instock availability').text

        dic = {
            'title' : title,
            'currency': price[0],
            'amount' : price[1:],
            'availabe' : available
        }
        books.append(dic)

    return books

all_books = books_scrapper(url)

with open('file1.csv','w', newline='') as f:
    writer = csv.DictWriter(f , fieldnames=books[0].keys())
    writer.writeheader()
    writer.writerows(all_books)

with open('file2.json','w') as f:
    json.dump(all_books, f , indent = 2, ensure_ascii=False )

    
