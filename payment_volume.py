import urllib, json, time, datetime
start = time.time()
while(True):
    now = datetime.datetime.now()
    url = "https://data.ripple.com/v2/network/payment_volume"
    with open('dump', 'a') as outfile:
        response = urllib.urlopen(url)
        data = json.loads(response.read())
        volume = data['rows'][0]['total']
        outfile.write(str(volume) + ' ' + str(now) + '\n')
        time.sleep(60.0 - ((time.time() - start) % 60.0))
