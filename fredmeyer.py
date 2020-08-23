# https://www.fredmeyer.com/p/clorox-disinfecting-wipes-value-pack/0004460030208

import requests
from bs4 import BeautifulSoup
from notify_run import Notify 

import requests

notify = Notify() 

threePack = "https://www.fredmeyer.com/p/clorox-disinfecting-wipes-value-pack/0004460030208"
fourPack = "https://www.fredmeyer.com/p/clorox-disinfecting-wipes-multi-pack/0004460031162"

def checker (site, name):

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36', "Upgrade-Insecure-Requests": "1","DNT": "1","Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8","Accept-Language": "en-US,en;q=0.5","Accept-Encoding": "gzip, deflate"}
    response = requests.get(site, headers=headers)
    soup =  BeautifulSoup(response.content, "html.parser")

    ship_data = soup.find('label', attrs={"for": "DELIVERY"})
    
    status = ship_data.text
    print(status)
    
    if "Unavailable" not in status:
        notify.send(name + ": " + status)

def runCheck():
    checker(threePack, "Clorox Three Pack Status:")
    checker(fourPack, "Clorox Four Pack Status:")
