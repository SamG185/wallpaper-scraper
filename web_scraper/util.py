import requests
import random
from bs4 import BeautifulSoup



baseUrl = "https://wallpapers.com"



url = "https://wallpapers.com/space"

pictureUrlThumbnails = []
pictureWebpages = []


#get raw page data from input
def getdata(url): 
    r = requests.get(url) 
    return r.text 

#parse raw data and return a list of direct image URLS from the input
def getListOfWallpapers():
    
    htmldata = getdata(url) 
    soup = BeautifulSoup(htmldata, 'html.parser') 
    pages = []
    for item in soup.find_all('img'):
        try:
            pages.append(baseUrl + "/images/high/" + item['data-src'].split("thumbnail/")[1].split(".")[0] + ".jpg")
        except:
            pass
    return pages



#pick random wallpaper from image URLS returned by getListOfWallpapers()
def getRandomWallpaper(list):
    return random.choice(list)

def writeImageToFile(url):
    response = requests.get(url)

    file = open("sample_image.png", "wb")
    file.write(response.content)
    file.close()
    print(file)