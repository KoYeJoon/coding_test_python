#request
import requests

target = "http://google.com"
response = requests.get(url=target)
print(response.text)

# json
import json

user = {
    "id" : "gildong",
    "password" : "192837",
    "age" : 30,
    "hobby" : ["football", "programming"]
}

#encoding : 파이썬 변수를 json 객체로 변환 (띄어쓰기 네 칸 들여쓰기 적용 )
json_data = json.dumps(user, indent=4)
print(json_data)


#decoding:  json -> python 자료형 : json.loads() 이용
data = json.loads(json_data)
print(data)


# json 으로 변환하여 json 파일 생성하기
with open("user.json","w",encoding="utf-8") as file:
    json.dump(user, file, indent=4)