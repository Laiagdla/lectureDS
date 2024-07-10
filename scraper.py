import requests
from bs4 import BeautifulSoup


url = 'http://localhost:8000/webpage.html'
url_imdb = 'https://www.imdb.com/list/ls055386972/'

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:126.0) Gecko/20100101 Firefox/126.0",
    "Accept-Language":"en-US"
}

response = requests.get(url_imdb, headers=headers)

soup = BeautifulSoup(response.content, "html.parser")
# movie = soup.find('li', class_= 'ipc-metadata-list-summary-item')
# print(movie.find('h3').string)

movies = soup.find_all('li', class_= 'ipc-metadata-list-summary-item')
for movie in movies:
    print(movie.find('h3').string)
