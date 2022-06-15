#!/usr/bin/env python3
from asyncio import exceptions
from urllib.error import HTTPError

import os
import threading
import requests

path = '../getcat/img/'
url = "https://cataas.com/cat"

def createFolder(path):
        try:
            if os.path.isdir(path):
                pass                
            else:
                os.makedirs(path)
                print('created directory for storing.')
        except IOError as exception:
            raise IOError('%s: %s' % (path, exception.strerror))
        return None


def downloadCat(name):
    print(f'[{name}] started download function')
    r = requests.get(url)
    hdr = r.headers['content-type']

    if hdr == 'image/jpeg':
        open(f'{path}cat{name}.jpeg', 'wb').write(r.content)
        print(f'downloading cat{name}')
    elif hdr == 'image/png':
        open(f'{path}cat{name}.png', 'wb').write(r.content)
        print(f'downloading cat{name}')
    else:
        print('\n NEW TYPE FOUND',type(hdr),'\n')
        
if __name__ == '__main__':
    createFolder(path)
    num = int(input('number of downloads: '))

    try:
        for n in range(num):    
            thread = threading.Thread(group=None,target=downloadCat,args=(n,))
            thread.start()
            thread.join()

    except requests.exceptions.HTTPError() as err:
        raise SystemExit(err)
    except requests.exceptions.ConnectionError() as err:
        raise SystemExit(err)
