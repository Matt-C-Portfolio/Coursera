
import json
import urllib.request, urllib.parse, urllib.error
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL: ')
uh = urllib.request.urlopen(url,context=ctx)
data = uh.read()

info = json.loads(data)
#print(info)
sum = 0

for item in info['comments']: 
    count = item['count']
    sum = sum + count

print(sum)
