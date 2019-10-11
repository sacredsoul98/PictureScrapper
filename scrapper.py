#program to scrape pics from an website
import requests
from bs4 import BeautifulSoup as bs
import os

url=input("Enter the URL you want to scrape ---")
#download page for parsing
page=requests.get(url)
soup=bs(page.text,'html.parser')
print("It's happening")
#locate all elements with image tags
image_tags=soup.findAll('img')

#create directory for downloaded pics
folders=input("Enter the folder name you want to create--")
if not os.path.exists(folders):
	os.makedirs(folders)


#move to new directory
os.chdir(folders)


#image file number variable
x=0

#downloading and loading pics into the folder
for image in image_tags:
	print("# ")
	try:
		url=image['src']
		source=requests.get(url)
		if source.status_code==200:
			with open('pic'+str(x)+'.jpg','wb') as f:
				f.write(requests.get(url).content)
				f.close()
				x+=1
				if x==100:
					break
	except:
		pass
print("Over")
