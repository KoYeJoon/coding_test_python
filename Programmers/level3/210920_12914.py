def factorial(n) :
    k=1
    for i in range(1,n+1):
        k *= i
    return k

def solution(n):
    answer = 0
    for even_num in range(n//2+1):
        odd_num = n-even_num*2
        answer += factorial(odd_num+even_num) // (factorial(odd_num)*factorial(even_num))
    return answer%1234567

print(solution(4))