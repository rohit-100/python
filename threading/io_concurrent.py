import requests
import time
import concurrent.futures
import threading


thread_local = threading.local()

def get_session():
    if not hasattr(thread_local,"session"):
        thread_local.session = requests.Session()
    return thread_local.session


def download_site(url):
    session = get_session()
    with session.get(url) as response:
        print(len(str(response)))


def download_all_sites(sites):
    with concurrent.futures.ThreadPoolExecutor(max_workers = 35) as executer:
        executer.map(download_site,sites)
        
if __name__ == "__main__":
    sites = ["http://jython.org"]*50

    start_time = time.time()
    download_all_sites(sites)
    duration = time.time() - start_time
    print("total duration is {}".format(duration))
    
