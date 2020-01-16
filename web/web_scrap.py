#https://www.fortytwo.sg/dining/dining-tables/ross-dining-table-walnut.html

import bs4
import requests

requestObj = requests.get("https://www.fortytwo.sg/dining/dining-tables/ryder-round-table-white.html")
requestObj.raise_for_status()
soup = bs4.BeautifulSoup(requestObj.text, 'html.parser')
elements = soup.select("#product-price-25086")
print(elements[0].text)


