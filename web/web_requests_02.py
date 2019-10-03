import requests

url="https://api.data.gov.sg/v1/environment/2-hour-weather-forecast"
req=requests.get(url)

try:
    req.raise_for_status()
    
    playFile = open("downloadedFile.txt","wb")
    for chunk in req.iter_content(1000000):
        print(chunk)
        playFile.write(chunk)
    playFile.close()
    
except Exception as e:
    print("There was a problem: %s" % (e))