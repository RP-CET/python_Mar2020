#https://www.fortytwo.sg/dining/dining-tables/ross-dining-table-walnut.html

import bs4
import requests
import openpyxl
import datetime

requestObj = requests.get("https://www.bookdepository.com/Life-Changing-Magic-Tidying-Marie-Kondo/9780091955106?ref=grid-view")
requestObj.raise_for_status()
soup = bs4.BeautifulSoup(requestObj.text, 'html.parser')
elements = soup.select("span.sale-price")
print(elements[0].text)

workbook = openpyxl.Workbook()
sheet=workbook["Sheet"]

sheet['A1'].value = elements[0].text
sheet['A2'].value = datetime.datetime.now()

workbook.save("web_scrapped_data.xlsx")


