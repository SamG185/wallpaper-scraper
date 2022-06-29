from posixpath import expanduser
import requests, random, shutil, os

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
            pages.append(baseUrl + "/images/hd/" + item['data-src'].split("thumbnail/")[1].split(".")[0] + ".jpg")
        except:
            pass
    return pages



#pick random wallpaper from image URLS returned by getListOfWallpapers()
def getRandomWallpaper(list):
    return random.choice(list)

def writeImageToFile(url):
    
    #get filename and set up path to save.
    filename = url.split("/")[-1]
    save_path = os.path.join('Pictures', 'Wallpapers')
    
    
    #check if directory exits, if not create it.
    isExist = os.path.exists(save_path)
    if not isExist:
        os.makedirs(save_path)
    
    
    
    #set path and add the filename
    full_path = os.path.join(save_path, filename)
    response = requests.get(url, stream = True)
    
    #check to ensure website hasn't thrown an error.
    if response.status_code == 200:
        #set this to true else downloaded image file size will be 0
        response.raw.decode_content = True
        with open(full_path, 'wb') as f:
            shutil.copyfileobj(response.raw, f)
        
        print("Success " + filename)
    else:
        print("failure")