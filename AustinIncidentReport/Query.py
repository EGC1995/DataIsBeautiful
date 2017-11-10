#!/usr/bin/env python

# make sure to install these packages before running:
# pip install pandas
# pip install sodapy

import pandas as pd
import requests
import numpy as np
import json
import matplotlib
from bokeh.plotting import figure, output_file, show

response = requests.get("https://data.austintexas.gov/resource/rkrg-9tez.json")
data = response.json()

print(response.status_code)
df = pd.DataFrame(data)
print(df.columns)

crimes = df['crime_type']
latitude = df['latitude']
longitude = df['longitude']
time = df['time']
date = df['date']

output_file("plot.html")

x = [1, 2, 3, 4, 5]
y = [6, 7, 2, 4, 5]
p = figure(title="crimes over time", x_axis_label = 'x', y_axis_label = 'y')
p.line(x,y, legend = "Temp.", line_width = 2)
show(p)
