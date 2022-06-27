import requests
from bs4 import BeautifulSoup



baseUrl = "https://wallpapers.com"



url = "https://wallpapers.com/space"

pictureUrlThumbnails = []
pictureWebpages = []


def getdata(url): 
    r = requests.get(url) 
    return r.text 

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

print(getListOfWallpapers())

