import requests

url = "https://api.data.gov.sg/v1/environment/2-hour-weather-forecast"
req = requests.get(url)
print(req.text)


