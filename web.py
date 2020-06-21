from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
import re

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


pos = input('enter pos:')
pos = int(pos)
rept = input('repeat n time')
rept = int(rept)
for i in range(rept):
    if i==0:
        url = input('Enter - ')
    else:
        url = nurl
    html = urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, "html.parser")
    tags = soup('a')
    cot = 0
    for tag in tags:
        cot = cot+1
        if cot == pos:
            print(tag.contents[0])
            nurl = tag.get('href', None)

    # print('TAG:', tag)
    # print('URL:', tag.get('href', None))
    # print('Contents:', tag.contents[0])
    # print('Attrs:', tag.attrs)


