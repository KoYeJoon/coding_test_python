# def solution(s):
#     temp = []
#     temp_s = ''
#     for i in s :
#         if i == ' ':
#             temp.append(int(temp_s))
#             temp_s = ''
#         else :
#             temp_s += i
#     temp.append(int(temp_s))
#
#     return str(min(temp)) + " " + str(max(temp))
def solution(s):
    s = list(map(int,s.split()))
    return str(min(s)) + " " + str(max(s))


print(solution("1 2 3 4"))