import requests

# REST API에 접속하여 response 데이터 받아오기
target = "https://jsonplaceholder.typicode.com/users"
response = requests.get(url=target)

# 응답 데이터가 json 형태이므로, 파이썬 객체로 반환
data = response.json()

# 모든 사용자(user)정보를 확인하며 이름 정보만 삽입
name_list = []
for user in data:
    name_list.append(user['name'])

print(name_list)