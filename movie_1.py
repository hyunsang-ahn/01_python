import requests
import json
import os
import csv
f = open("boxofiice.csv", "a+", encoding="utf-8", newline="")
csv_m = csv.writer(f)
key = os.getenv("KOBIS_KEY")
day = ['20190113', '20190106', '20181230', '20181223', '20181216', '20181209', '20181202', '20181125', '20181118', '20181111']

movie_name = []
for d in day:
    r = requests.get(f"http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchWeeklyBoxOfficeList.json?key={key}&targetDt={d}&weekGb=0")
    res = r.json()
    for i in range(10):
        name = res['boxOfficeResult']['weeklyBoxOfficeList'][i]['movieNm']
        code = res['boxOfficeResult']['weeklyBoxOfficeList'][i]['movieCd']
        acount = res['boxOfficeResult']['weeklyBoxOfficeList'][i]['audiAcc']
        if name not in movie_name:
            movie_name.append(name)
            csv_m.writerow([name, code, acount, d])
        # if name not in movie_name:
        #     movie_name.append(name)
        #     print(movie_name)
            # csv_m.writerow([movie_name, code, acount, d])
       
    #   for i in range(10):
        #     print("무비네임 : " + res['boxOfficeResult']['weeklyBoxOfficeList'][i]['movieNm'])
        #     print("무비코드 : " + res['boxOfficeResult']['weeklyBoxOfficeList'][i]['movieCd'])
        #     print("관객수 : " + res['boxOfficeResult']['weeklyBoxOfficeList'][i]['audiAcc'])
        #     print("조사날짜 : " + d)
        #     print()
    

f.close()




#kobis_key= os.getenv('KOBIS_KEY')
     
     