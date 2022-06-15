#!/usr/bin/env python3
from asyncio import exceptions
from logging import raiseExceptions
from urllib.error import HTTPError

import threading
import requests

url = "https://cataas.com/cat"

def downloadPic(name):
    print('started downloading function')
    r = requests.get(url)
    hdr = r.headers['content-type']

    if hdr == 'image/jpeg':
        open(f'pic{name}.jpeg', 'wb').write(r.content)
        print(f'downloading pic{name}')
    elif hdr == 'image/png':
        open(f'pic{name}.png', 'wb').write(r.content)
        print(f'downloading pic{name}')
    else:
        print('\n NEW TYPE FOUND',type(hdr),'\n')
        
if __name__ == '__main__':
    num = 10 #int(input('number of downloads:'))

    try:
        for n in range(num):    
            print(n)    
            thread = threading.Thread(group=None,target=downloadPic,args=(n,))
            thread.start()
            thread.join()

    except requests.exceptions.HTTPError() as err:
        raise SystemExit(err)
    except requests.exceptions.ConnectionError() as err:
        raise SystemExit(err)
