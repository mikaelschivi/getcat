#!/usr/bin/env python3
from asyncio import exceptions
from logging import raiseExceptions
from urllib.error import HTTPError

import threading
import requests

url = "https://cataas.com/cat"
r = requests.get(url)

def downloadPic(name):
    print('fetching...')
    hdr = r.headers['content-type']

    if hdr == 'image/jpeg':
        open(f"pic{name}.jpeg", 'wb').write(r.content)
        print(f'DOWNLOADING [ID {name}] [TYPE {hdr}]...')
    elif hdr == 'image/png':
        open(f"pic{name}.png", 'wb').write(r.content)
        print(f'DOWNLOADING [ID {name}] [TYPE {hdr}]...')
    else:
        print(type(hdr))
        
if __name__ == '__main__':
    num = 10 #int(input('number of downloads:'))

# FIX THIS SHIT
    try:
        for n in range(num):    
            
            thread = threading.Thread(downloadPic(n),args=(n,))
            thread.start()

    except requests.exceptions.HTTPError() as err:
        raise SystemExit(err)   
