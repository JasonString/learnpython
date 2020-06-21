import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
x = urllib.request.urlopen(url, context=ctx).read()
tree = ET.fromstring(x)
counts = tree.findall('comments/comment')
s= 0
for i in counts:
    val = int(i.find('count').text)
    s = s + val
print(s)