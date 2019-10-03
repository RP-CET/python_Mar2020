import openpyxl
from openpyxl.chart import BarChart, Reference

workbook = openpyxl.Workbook()

# create a list of tuples as data source
data = [
  ('Name','Admission'),
  ('Gone with the Wind',225.7),
  ('Star Wars',161.0),
  ('ET: The Extraterrestrial',161.0)
  ]
   
sheet = workbook['Sheet']
for row in data:
  sheet.append(row)
  
chart = BarChart()
chart.title = "Admissions per movie"
chart.y_axis.title = "Millions"

#create a reference to the data, and append the data to chart
data = Reference(sheet, min_row=2, max_row=4, min_col=1, max_col=2)
chart.add_data(data, from_rows=True, titles_from_data=True)

sheet.add_chart(chart, "A6")
workbook.save("movie_chart.xlsx")