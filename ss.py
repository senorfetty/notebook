import urllib.parse, urllib.request
import json


servurl= 'http://maps.googleapis.com/maps/api/geocode/json?'

while True:
    address= input('Location: ')
    if len(address) < 1:
        break
    url= servurl + urllib.parse.urlencode({'address' : address})
    print('Retrieving: ', url)
    uh= urllib.request.urlopen(url)
    data= uh.read().decode()
    print(len(data))

    try:
        js= json.loads(data)

    except:
        js= None

    if not js or 'status' not in js or js['status'] != 'OK':
        print('=== FAILED ===')
        print(data)
        continue

    lat = js["results"][0]["geometry"]["location"]["lat"]
    lng = js["results"][0]["geometry"]["location"]["lng"]
    print(lat, lng)

    loc= js["results"][0]["formatted_address"]
    print(loc)

    