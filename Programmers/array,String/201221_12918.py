def solution(s):
    return True if s.isdigit() and (len(s)==4 or len(s)==6) else False

s="a234a"
print(solution(s))