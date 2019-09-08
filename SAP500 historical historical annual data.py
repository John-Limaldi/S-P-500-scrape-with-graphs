# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 18:08:41 2019

@author: John Limaldi
"""

import requests
from bs4 import BeautifulSoup
from matplotlib import pyplot as plt
import pandas as pd
import numpy as np

url = "https://www.macrotrends.net/2324/sp-500-historical-chart-data"

headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36"}

response = requests.get(url, headers =  headers)

soup = BeautifulSoup(response.content, "html.parser")

stat_table = soup.find_all("tbody")

stat_table = stat_table[0]

with open ("SAP_over_time", "w") as r:
    for row in stat_table.find_all("tr"):
        for cell in row.find_all("td"):
           r.write(cell.text.ljust(9))
        r.write("\n")
        
df = pd.read_csv("SAP_over_time",header = None, engine = "python", delimiter=r"\s+")
df.columns = ["Year", "Avg_Closing_Price", "Year_Open", "Year_High", "Year_Low", "Year_ Close", "Annual_%_Change"]
print(df)


df["Year"].astype(float)
df["Avg_Closing_Price"] = df["Avg_Closing_Price"].str.replace(",","").astype(float)
df["Year_Open"] = df["Year_Open"].str.replace(",","").astype(float)
df["Year_High"] = df["Year_High"].str.replace(",","").astype(float)
df["Year_Low"] = df["Year_Low"].str.replace(",","").astype(float)
df["Year_ Close"] = df["Year_ Close"].str.replace(",","").astype(float)
df["Annual_%_Change"] = df["Annual_%_Change"].str.replace("%","")
df["Annual_%_Change"] = df["Annual_%_Change"].str.replace(",","").astype(float)

ax = plt.gca()
df.plot(kind = "line", x = "Year", y = "Avg_Closing_Price", ax = ax)
df.plot(kind = "line", x = "Year", y = "Year_Open", color = "red", ax = ax)
df.plot(kind = "line", x = "Year", y = "Year_High", color = "blue", ax = ax)
df.plot(kind = "line", x = "Year", y = "Year_Low", color = "yellow", ax = ax)
df.plot(kind = "line", x = "Year", y = "Year_ Close", ax = ax)
df.plot(kind = "line", x = "Year", y = "Annual_%_Change", ax = ax)
plt.show()



