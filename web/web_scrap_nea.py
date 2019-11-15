import bs4
import requests
import openpyxl
import datetime

requestObj = requests.get("http://www.weather.gov.sg/weather-currentobservations-temperature")
requestObj.raise_for_status()
soup = bs4.BeautifulSoup(requestObj.text, 'html.parser')

#locate a location
data = soup.find("span", {"id": "S121"})
print (data.text)


data = soup.find("div", {"id": "sg_region_popover"})
children = data.findChildren("span" , recursive=False)
towns = []
for i in children:
    tmp = i["data-content"]
    marker1 = tmp.find("<strong>")
    marker2 = tmp.find("</strong>")
    location = tmp[marker1 + 8:marker2]
    print (location + " : " + i.text)
    towns.append([location, i.text])

