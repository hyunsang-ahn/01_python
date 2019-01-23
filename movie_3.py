import requests
import json
import os
import csv

naver_client_id = os.getenv('NAVER_ID')
naver_client_secret = os.getenv('NAVER_SECRET')

f = open("movie_naver.csv", "a+", encoding='utf-8', newline="")
f2 = open("movie.csv", "r", encoding="utf-8")
csv_r = csv.reader(f2)
for line in csv_r:
    m = requests.get("https://openapi.naver.com/v1/search/movie?query={}".format(line[1]),
                    headers = {
                        "X-Naver-Client-Id":naver_client_id,
                        "X-Naver-Client-Secret":naver_client_secret
                    }
        )

    res = m.json()
    name = line[0]
    image_url = res['items'][0]['image']
    h_link = res['items'][0]['link']
    userRating = res['items'][0]['userRating']
    csv_w = csv.writer(f)
    csv_w.writerow([name,image_url,h_link,userRating])
    
f.close()   
f2.close()

