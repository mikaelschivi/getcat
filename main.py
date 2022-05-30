#!/usr/bin/env python3
from asyncio import exceptions
from logging import raiseExceptions
from socket import timeout
from urllib.error import HTTPError
import requests

inp = int(input('number of downloads:'))
url = "https://cataas.com/cat"

print('fetching...')
for Id in range(inp):
    try:
        r = requests.get(url,timeout=5)
        r.raise_for_status()
        
        hdr = r.headers['content-type']
        if hdr == 'image/jpeg':
            open(f"pic{Id}.jpeg", 'wb').write(r.content)
            print(f'downloading {hdr}...')
        else:
            open(f"pic{Id}.png", 'wb').write(r.content)
            print(f'downloading {hdr}...')

        print('ok')

    except requests.exceptions.HTTPError() as err:
        raise SystemExit(err)
