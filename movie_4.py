import requests
import json
import os
import csv


f = open("movie_naver.csv", "r", encoding="utf-8")
csv_r = csv.reader(f)
for line in csv_r:
    url = line[1]
    res = requests.get(url)
    with open('./images/{}.jpg'.format(line[0]),'wb') as f:
        f.write(res.content)