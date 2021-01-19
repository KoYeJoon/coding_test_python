import re

def solution(files):
    a = sorted(files, key=lambda file : int(re.findall('\d+', file)[0]))
    b = sorted(a, key=lambda file : re.split('\d+', file.lower())[0])
    return b

# def solution(files):
#     temp = []
#     answer = []
#     for i in files :
#         head = []
#         number = []
#         tail = []
#         flag = 0
#         for j in range(len(i)):
#             if i[j].isdigit() :
#                 number.append(i[j])
#                 flag = 1
#             elif flag == 0 and not i[j].isdigit() :
#                 head.append(i[j])
#             elif flag == 1 and not i[j].isdigit() :
#                 tail = i[j:]
#                 break
#
#         temp.append([''.join(head),''.join(number),''.join(tail)])
#
#     temp = sorted(temp,key = lambda x : (x[0].lower(), int(x[1])))
#
#     for i in temp :
#         answer.append(''.join(i))
#
#     return answer

print(solution( ['F-5 Freedom Fighter', 'B-50 Superfortress', 'A-10 Thunderbolt II','F-14 Tomcat']))