import json
import requests

url="https://api.data.gov.sg/v1/environment/2-hour-weather-forecast"
req=requests.get(url)

data = json.loads(req.text)

forecasts = data["items"][0]["forecasts"]

for forecast in forecasts:
    area = forecast["area"]
    weather = forecast["forecast"]
    print(area + ": " + weather)
    