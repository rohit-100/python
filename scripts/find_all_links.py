import requests
import re

url = input('enter the url\n')

website = requests.get(url)

html = website.text

links = re.findall('"((http|ftp)s?://.*?)"',html)

for link in links :
	print(link)
	
