1. 영화진흥위원회의 키값을 따라서

    r = requests.get(f"http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchWeeklyBoxOfficeList.json?key={key}&targetDt={d}&weekGb=0")


url의 요청값을 통해서 내가 원하는 정보를 추출함.

그 이후 최근 10주간의 데이터중 주간 박스오피스 10개의 데이터를 수집완료함.

마지막으로 수집된 데이터의 중복방지를 위해서


        if name not in movie_name:
            movie_name.append(name)
            csv_m.writerow([name, code, acount, d])
            
코드를 통해서 중복된 값을 제거하여 총 43개의 데이터를 수집



2. 1번 프로젝트를 통해서 얻을 영화의 제목을 따로 추출함.
c_reader = csv.reader(open('boxofiice.csv', 'r'))

영화제목을 기준으로 url 과 키값을 통해서

영화코드 영화명, 개봉연도, 상영시간, 장르,감독, 등급,배우등 데이터를 수집

배우가 3명이하인 데이터에 대해서 빈값을 주기위해서

if size >= 3:
        ac1 = res["movieInfoResult"]["movieInfo"]["actors"][0]['peopleNm']
        ac2 = res["movieInfoResult"]["movieInfo"]["actors"][1]['peopleNm']
        ac3 = res["movieInfoResult"]["movieInfo"]["actors"][2]['peopleNm']
    elif size == 2:
        ac1 = res["movieInfoResult"]["movieInfo"]["actors"][0]['peopleNm']
        ac2 = res["movieInfoResult"]["movieInfo"]["actors"][1]['peopleNm']
    elif size == 1:
        ac1 = res["movieInfoResult"]["movieInfo"]["actors"][0]['peopleNm']
        
        코드를 사용하여 배우 숫자에 따른 빈값을 지정해줌
        
        
3. 2번프로젝트를 통해서 얻을 영화명(국문)의 데이터를 통해서 네이버 영화 검색을 실시

f2 = open("movie.csv", "r", encoding="utf-8")
csv_r = csv.reader(f2)

이용하여 2번프로젝트의 데이터를 3번 프로젝트에서 이용한다.

naver_client_id = os.getenv('NAVER_ID')
naver_client_secret = os.getenv('NAVER_SECRET')

네이버의 키값과 url을 통해서 네이버 api를 이용한다

for line in csv_r:
    m = requests.get("https://openapi.naver.com/v1/search/movie?query={}".format(line[1]),
                    headers = {
                        "X-Naver-Client-Id":naver_client_id,
                        "X-Naver-Client-Secret":naver_client_secret
                    }
        )
        
를 통해서 네이버 키값과 url을 통해서 

영진위 영화 대표코드 썸네일 이미지 url
하이퍼텍스트 link 유저평점을 추출함.

4. 앞서 얻은 이미지 url을 통해서 실제 이미지파일로 저장함.
for line in csv_r:
    url = line[1]
    res = requests.get(url)
    with open('./images/{}.jpg'.format(line[0]),'wb') as f:
        f.write(res.content)


'
'

# 01_python
