# https://www.fredmeyer.com/p/clorox-disinfecting-wipes-value-pack/0004460030208

import requests
from bs4 import BeautifulSoup
from notify_run import Notify 
from sense_hat import SenseHat

import requests


sense = SenseHat()
notify = Notify() 

threePack = "https://www.fredmeyer.com/p/clorox-disinfecting-wipes-value-pack/0004460030208"
fourPack = "https://www.fredmeyer.com/p/clorox-disinfecting-wipes-multi-pack/0004460031162"

def checker (site, name):

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36', "Upgrade-Insecure-Requests": "1","DNT": "1","Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8","Accept-Language": "en-US,en;q=0.5","Accept-Encoding": "gzip, deflate"}
    response = requests.get(site, headers=headers)
    soup =  BeautifulSoup(response.content, "html.parser")

    ship_data = soup.find('label', attrs={"for": "SHIP"})
    
    status = ship_data.text
    return status

def runCheck():
    
    threePackResult = checker(threePack, "Clorox Three Pack Status:")
    fourPackResult = checker(fourPack, "Clorox Four Pack Status:")
    if "Unavailable" not in threePackResult and "Unavailable" not in fourPackResult:
        notify.send("Three Pack Result: " + threePackResult + " Four Pack Result: " + fourPackResult)
        print("Notification Sent")
        O = [0, 255, 0]

    else:
        O = [255, 0, 0] 

    display = [
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O
    ]

    sense.set_pixels(display)
        
           
    print("Three Pack Result: " + threePackResult + " Four Pack Result: " + fourPackResult)

runCheck()