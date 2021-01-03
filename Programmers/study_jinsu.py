# 반복문 버전
def jinsu(a,b):
    convertString="0123456789ABCDEF"
    sol=''
    if a<b :
        return convertString[a]
    while a>=b:
        n=divmod(a,b)
        a //= b
        sol += convertString[n[1]]
    sol += convertString[n[0]]
    return sol[::-1]

# 재귀법 버전
def jinsu_rec(a,b):
    convertString="0123456789ABCDEF"
    if a <b :
        return convertString[a]
    n = divmod(a,b)
    return jinsu_rec(a//b, b)+ convertString[n[1]]


a = int(input("진수를 변환하고 싶은 숫자를 입력하세요: "))
b = int(input("몇 진수로 변환하고 싶습니까?"))
print("반복문으로 구한 %d 의 %d 진수 변환 : %s" %(a,b,jinsu(a,b)))
print("재귀법으로 구한 %d 의 %d 진수 변환 : %s" %(a,b,jinsu_rec(a,b)))