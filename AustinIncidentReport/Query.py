#!/usr/bin/env python

# make sure to install these packages before running:
# pip install pandas
# pip install sodapy

import pandas as pd
import requests

response = requests.get("https://data.austintexas.gov/resource/rkrg-9tez.json")
print(response.status_code)
