import requests
import re
try:
    from urllib.parse import urljoin
except ImportError:
    from urlparser import urljoin

link_re = re.compile(r'href="(.*?)"')

def crawl(url):
    req = requests.get(url)

    if req.status_code != 200:
        print("status code is not 200")
        return []

    links = link_re.findall(req.text)

    print("\n found {} links".format(len(links)))

    for link in links:
        link = urljoin(url,link)
        print(link)
   


if __name__ == '__main__':
    crawl('https://www.geeksforgeeks.org/dynamic-programming/')