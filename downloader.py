# Downloader Image From Url
import os
from urllib.parse import urlparse
import urllib.request

listOfImages = open("zaros.txt").readlines()
#print(listOfImages[0])
photoCounter = len(listOfImages)
print(len(listOfImages))

i = 0
while i!=photoCounter:
	print("Image No: {}" .format(i))
	print(listOfImages[i])
	url = listOfImages[i]
	filename = url.split('/')[-1]
	filename = filename.rstrip("\n")
	#print(filename)
	a = urlparse(url)
	base = os.path.basename(a.path)
	print(base)
	urllib.request.urlretrieve(url,filename)
	print("Counter Left: {}".format(photoCounter-i))
	i = i + 1
