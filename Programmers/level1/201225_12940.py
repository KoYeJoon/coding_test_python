def gcd(a,b) :
    if b==0 :
        return a
    return gcd(b,a%b)


def solution(n, m):
    answer = []
    gcd_nm = gcd(n,m)
    answer.append(gcd_nm)
    lcm_n = gcd_nm * (n//gcd_nm) * (m//gcd_nm)
    answer.append(lcm_n)
    return answer

print(solution(40,6))