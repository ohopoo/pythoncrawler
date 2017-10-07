import requests
from requests.auth import HTTPProxyAuth
from bs4 import BeautifulSoup
import cssutils
import movie
import fresh_tomatoes

URL = "https://phimmoi.net/"
# proxies = {'http': 'http://proxy.dad.gameloft.org/proxy.pac'}
# auth = HTTPProxyAuth("hop.duongthanh@gameloft.com", "Duth@h0gl09")

movies_list = []
movies = []

def getUrlResponse(url):
    return requests.get(url)#, proxies=proxies, auth=auth)

def crawler(html):
    for movie_item in html.find_all('li', class_='movie-item'):
        title = movie_item.find('span', class_='movie-title-2').get_text()
        div_style = movie_item.find('div', class_='movie-thumbnail')['style']
        poster_style = cssutils.parseStyle(div_style)
        href = movie_item.find('a')['href']

        trailer_response = getUrlResponse(URL + href)
        trailer_html = BeautifulSoup(trailer_response.content, 'html.parser')
        trailer_url = trailer_html.find(id='btn-film-trailer')
        if trailer_url is not None:
            movies_list.append({'title': title, 'poster': poster_style['background'][4:-1], 'url': trailer_url['data-videourl']})

url = URL + 'trailer/'
while url is not None:
    response = getUrlResponse(url)
    html = BeautifulSoup(response.content, 'html.parser')
    crawler(html)
    pages_html = html.find('ul', class_='pagination pagination-lg')
    if pages_html is not None:
        pages = pages_html.select('li a')
        if pages is not None and 'kế' in pages[len(pages) - 1].get_text():
            url = URL + pages[len(pages) - 1]['href']
        else:
            url = None
    else:
        url = None


#Creating instances of my movie class with a list of my favorite movies.
for m in movies_list:
    movies.append(movie.Movie(m['title'],
                                  m['poster'].replace('http:', 'https:'),
                                  m['url'].replace('http:', 'https:')))

print(movies_list)
if len(movies) > 0:
    fresh_tomatoes.open_movies_page(movies)