import requests
from geopy.geocoders import Nominatim
import re

base_url = 'https://www.yogiyo.co.kr/api/v1/'   # 요기요 링크

def geocoding(address): # 주소를 위도, 경도로 변환
    # 주소의 범위를 대한민국으로 한정
    geolocoder = Nominatim(user_agent = 'South Korea', timeout=None)
    geo = geolocoder.geocode(address)
    # crd 사전에 대구 태전동의 lat=위도/ lng=경도를 넣음
    crd = {"lat": str(geo.latitude), "lng": str(geo.longitude)}
    # 위도와 경도가 담긴 crd 반환
    return crd


crd = geocoding("경기도 광명시") # 어디를 검색할 것인지

headers = {
    'x-apikey': 'iphoneap',
    'x-apisecret': 'fe5183cc3dea12bd0ce299cf110a75a2'
}

res = requests.get(f"{base_url}restaurants-geo/?items=60&lat={crd['lat']}&lng={crd['lng']}&order=rank&page=0", headers=headers)


for p in range(res.json()['pagination']['total_pages']+1): 
    res = requests.get(f"{base_url}restaurants-geo/?items=60&lat={crd['lat']}&lng={crd['lng']}&order=rank&page={p}", headers=headers)
    
    for item in res.json()['restaurants']:  # restaurants 안에 있는 item들을 반복
        print(item['name'], item['address'])    # item의 name과 address 출력
        
        #층수만 출력
#        floor = re.search("\w+[층]", item['address'])
#        floor = floor.group() if floor != None else None 
#        print(floor)