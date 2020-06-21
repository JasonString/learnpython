import urllib.request, urllib.parse, urllib.error
import ssl
import json

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input("URL:"  )
if len(url)<1:
    url = "http://py4e-data.dr-chuck.net/comments_689722.json"
data = urllib.request.urlopen(url).read().decode()
js = json.loads(data)
num = 0
i = 0
while True:
    try:
        num = num + int( js['comments'][i]['count']  )
        i = i+1
    except:
        break
print(num)


    