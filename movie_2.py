import requests
import json
import os
import csv
f = open("movie.csv", "a+", encoding="utf-8", newline="")
csv_m2 = csv.writer(f)
key = os.getenv("KOBIS_KEY")


c_reader = csv.reader(open('boxofiice.csv', 'r'))

# say you want the second column, only...
col_2 = list(zip(*c_reader))[1] # keeping in mind that python is 0-indexed

# or if you want to come back for more later on, you can just do...
columns = list(zip(*c_reader))




for col in col_2:
    r = requests.get(f"http://www.kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieInfo.json?key={key}&movieCd={col}")
    res = r.json()
    name = res["movieInfoResult"]['movieInfo']["movieNm"]
    code = res["movieInfoResult"]['movieInfo']["movieCd"]
    name_kr = res["movieInfoResult"]['movieInfo']["movieNm"]
    name_en = res["movieInfoResult"]['movieInfo']["movieNmEn"]
    name_or = res["movieInfoResult"]['movieInfo']["movieNmOg"]
    year = res["movieInfoResult"]['movieInfo']["prdtYear"]
    time = res["movieInfoResult"]['movieInfo']["showTm"]
    zal = res["movieInfoResult"]["movieInfo"]["genres"][0]['genreNm']
    coach = res["movieInfoResult"]["movieInfo"]["directors"][0]['peopleNm']
    tier = res["movieInfoResult"]["movieInfo"]["audits"][0]['watchGradeNm']
    ac1 = ""
    ac2 = ""
    ac3 = ""
    
    size = len(res["movieInfoResult"]["movieInfo"]["actors"])
    
    if size >= 3:
        ac1 = res["movieInfoResult"]["movieInfo"]["actors"][0]['peopleNm']
        ac2 = res["movieInfoResult"]["movieInfo"]["actors"][1]['peopleNm']
        ac3 = res["movieInfoResult"]["movieInfo"]["actors"][2]['peopleNm']
    elif size == 2:
        ac1 = res["movieInfoResult"]["movieInfo"]["actors"][0]['peopleNm']
        ac2 = res["movieInfoResult"]["movieInfo"]["actors"][1]['peopleNm']
    elif size == 1:
        ac1 = res["movieInfoResult"]["movieInfo"]["actors"][0]['peopleNm']
        
    csv_m2 = csv.writer(f)
    csv_m2.writerow([code, name_kr, name_en, name_or, year, time, zal, coach, tier, ac1, ac2, ac3])

f.close()