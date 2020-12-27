# 이해 필요 (이해하고 TIL에 작성하)
def gcd(a,b) :
    if b==0 :
        return a
    return gcd(b,a%b)

def solution(w,h):
    if w==h:
        return w**2 - w
    return w*h - (w+h-gcd(w,h))

print(solution(8,12))