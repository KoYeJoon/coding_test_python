# https://gosmcom.tistory.com/130
import requests
response = requests.get('https://api.githuub.com/events')
print(response.text)
response = requests.post('https://httpbin.org/post',data={'key':'value'})
response = requests.put('https://httpbin.org/put',data={'key':'value'})
response = requests.delete('https://httpbin.org/delete')
response = requests.head('https://httpbin.org/get')
response = requests.options('https://httpbin.org/get')

payload = {'key1':'value1','key2':'value2'}
response = requests.get('https://httpbin.org/get',params=payload)


import requests
# 웹요청 방식 - 정식
# 'https//search.naver.com/search.naver?query=아이스크림"
host = 'https//search.naver.com'
path = '/search.naver'
params = {'query' : '아이스크림'}
url = host + path

response = requests.get(url,params = params)

#응답 데이터 속성
print(response.status_code)#응답 상태 코드
print(response.url) # 요청했던 url
print(response.text) # 응답데이터 str- 웹페이지의 소스코드나 문자데이터, json 확인 싯
print(response.content) # 응답데이터 byte - 음악, 비디오 등 byte 자체를 받아 저장할 때
print(response.encoding) # 응답데이터의 인코딩 방식
print(response.headers) # 응답 데이터의 헤더

# 웹 요청 데이터의 header 변경
url = 'http://www.ichangtou.com/#company:data_000008.html'
headers = {'user-agent' : 'Chrome'}
response = requests.get(url,headers=headers)

# post 방식
data = {'key':'value'}
response = requests.post('https://httpbin.org/post',data=data)

url = 'https://httpbin.org/post'
files = {'file' : open('report.xls','rb')}
response = requests.post(url,files=files)

#json으로 보내는 경우
import json
url = 'https://api.github.com/some/endpoint'
payload = {'some':'data'}
response = requests.post(url, data=json.dumps(payload))

#curl 읽는법
# https://curl.trillworks.com/
'''
curl -v -X POST "https://kapi.kakao.com/v1/vision/face/detect" \
-d "image_url=https://t1.daumcdn.net/alvolo/_vision/openapi/r2/images/01.jpg" \
-H "Authorization: KakaoAK key"
'''

import requests

url = "https://kapi.kakao.com/v1/vision/face/detect"
data = {'image_url':"https://t1.daumcdn.net/alvolo/_vision/openapi/r2/images/01.jpg"}
header = {"Authorization":'KakaoAK key'}
res = requests.post(url,data=data, headers=header)
print(res.status_code)