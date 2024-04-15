#!/usr/bin/env python3
import os
import threading
import requests

path = '../getcat/img/'
url = "https://cataas.com/cat"
head = {
    'Host': 'cataas.com',
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:124.0) Gecko/20100101 Firefox/124.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate, br',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
   }

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
    while os.path.exists(f'../getcat/img/cat{n}.jpeg') or os.path.exists(f'../getcat/img/cat{n}.png'):
        n+=1
    return f'cat{n}.{imtype}'

def downloadCat():
    r = requests.get(url, headers=head)
    contentType = r.headers['content-type']

    if contentType == 'image/jpeg':
        open(path+nameCat('jpeg'), 'wb').write(r.content)
        print(f'downloading jpeg cat')
    elif contentType == 'image/png':
        open(path+nameCat('png'), 'wb').write(r.content)
        print(f'downloading png cat')
    elif type(contentType) == '<class str>':
        print(contentType)
    else:
        print('\n NEW TYPE FOUND',type(contentType),'\n')

if __name__ == '__main__':
    createFolder(path)
    num = int(input('how many cute pics u want? '))

    try:
        for n in range(num):
            thread = threading.Thread(target=downloadCat)
            thread.start()
        print('fetching...')
    except requests.exceptions.HTTPError() as err:
        print(err)
    except Exception as e:
        print(e)