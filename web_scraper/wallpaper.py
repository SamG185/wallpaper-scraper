import requests, random, shutil, os, ctypes
from bs4 import BeautifulSoup
from PIL import Image



baseUrl = "https://wallpapers.com"
pictureUrlThumbnails = []
pictureWebpages = []


#get raw page data from input
def getdata(url): 
    r = requests.get(url) 
    return r.text 

#parse raw data and return a list of direct image URLS from the input
def getListOfWallpapers(genre):
    
    htmldata = getdata(baseUrl + "/" + genre) 
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
    save_path = os.path.join(os.path.expanduser('~'), "Pictures", "Wallpapers")
    
    
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
        
        
    else:
        print("response failure from webpage")
        
    
    #load the saved image into an Image object, check if landscape and if not rotate/save
    
    
    im = Image.open(full_path)
    if im.size[0] < im.size[1]:
        rotateAndSave(im, full_path)
        
    
		

    

    
def setDesktopBackground(wallpaper):
    image = wallpaper.split("/")[-1]
    
    #get the absolute path to the newly saved picture
    path = os.path.join(os.path.expanduser('~'), "Pictures", "Wallpapers", image)
    ctypes.windll.user32.SystemParametersInfoW(20, 0, path , 0)
    

def rotateAndSave(image, path):
    rotated_image = image.rotate(90, expand=1)
    rotated_image.save(path)
    