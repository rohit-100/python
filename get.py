import re
import requests

url = 'https://github.com/tr0j4n034/SPOJ'

r = requests.get(url)
r=r.text

pattern='......(.py|.cpp|.java)'
result = re.findall(pattern,r)
print(result)
