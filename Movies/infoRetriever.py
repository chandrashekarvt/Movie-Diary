from bs4 import BeautifulSoup
import requests
import random

# movie = 'thuppakki'
# mov = movie.lower()
# movie = mov.replace(' ', '-')

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36'
    }


def getRatings(movie):
    try:
        url1 = 'https://www.google.com/search?q={}'.format(movie)
        page1 = requests.get(url1, headers=headers)
        soup1 = BeautifulSoup(page1.content, 'html.parser')
        ratings = soup1.find(class_='gsrt IZACzd').get_text()
        return ratings
    except:
        return '8/10'


def getTitle(movie):
    title = None
    try:
        url = 'https://www.moviebuff.com/{}'.format(movie)
        page = requests.get(url, headers=headers)
        soup = BeautifulSoup(page.content, 'html.parser')
        title = soup.find(class_='col-sm-7').find('h1').get_text().strip()
        return title
    except:
        return None


def getImageUrl(movie):
    url = 'https://www.moviebuff.com/{}'.format(movie)
    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    image = soup.find_all(class_='col-md-6')[1].find_all(class_="gallery-title")
    index = 0
    for i in image:
        if i.get_text() == 'Posters':
            break
        index += 1

    image_url = soup.find_all(class_='col-md-6')[1].find_all(class_='gallery')[index]

    image_url1 = image_url.find_all('img')
    imgListNum = []
    for i in range(len(image_url1)):
        imgListNum.append(i)

    image_url1 = image_url.find_all('img')[random.choice(imgListNum)]

    image_src = image_url1['src']
    start = 'http://'
    final_image = start.__add__(image_src[2:])
    return final_image
