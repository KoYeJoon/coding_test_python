def solution(a, b):
    dayName=['THU','FRI','SAT','SUN','MON','TUE','WED']
    day=[31,29,31,30,31,30,31,31,30,31,30,31]
    temp = sum(day[:a-1])+b
    return dayName[temp%7]

print(solution(5,24))