import util




mylist = util.getListOfWallpapers()

wallpaperURL = util.getRandomWallpaper(mylist)

util.writeImageToFile(wallpaperURL)

