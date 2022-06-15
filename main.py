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
                print('created directory for storing cute pics.')
        except IOError as exception:
            raise IOError('%s: %s' % (path, exception.strerror))
        return None

def nameCat(imtype: str):
    n=0
    while os.path.exists(f'../getcat/img/cat{n}.jpeg') or os.path.exists(f'../getcat/img/cat{n}.png') == True:
        n+=1
    return f'cat{n}.{imtype}'

def downloadCat():
    r = requests.get(url)
    hdr = r.headers['content-type']

    if hdr == 'image/jpeg':
        open(path+nameCat('jpeg'), 'wb').write(r.content)
        print(f'downloading jpeg cat')
    elif hdr == 'image/png':
        open(path+nameCat('png'), 'wb').write(r.content)
        print(f'downloading png cat')
    else:
        print('\n NEW TYPE FOUND',type(hdr),'\n')

if __name__ == '__main__':
    createFolder(path)
    num = int(input('how many cute pics u want? '))

    try:
        for n in range(num):
            thread = threading.Thread(target=downloadCat)
            thread.start()
        print('fetching...')
    except requests.exceptions.HTTPError() as err:
        raise SystemExit(err)   