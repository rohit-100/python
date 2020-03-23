import requests
import time

def download_site(url):
    with session.get(url) as response:
        print(len(response))


def download_all_sites(sites):
    with requests.Session() as session:
        for url in sites:
            with session.get(url) as response:
                print(len(str(response)))

        
if __name__ == "__main__":
    sites = ["http://jython.org"]*80

    start_time = time.time()
    download_all_sites(sites)
    duration = time.time() - start_time
    print("total duration is %d".format(duration))


