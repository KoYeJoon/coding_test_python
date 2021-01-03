# def solution(s):
#     trans_s = s[1:-1]
#     s_arr=[]
#     count_s = trans_s.count("{")
#     answer = []
#     for i in range(count_s):
#         right = trans_s.index('}')
#         temp_s = trans_s[1:right]
#         s=''
#         temp = []
#         flag=0
#         for j in temp_s :
#             if j== ',' :
#                 flag=1
#                 if s != '':
#                     temp.append(int(s))
#                     s=''
#                 continue
#             else :
#                 s+=j
#         temp.append(int(s))
#         s_arr.append(temp)
#         trans_s = trans_s[right+2:]
#
#     s_arr.sort(key=lambda x : len(x))
#     len_s = len(s_arr)
#     for i in range(len_s):
#         answer.append(s_arr[i][0])
#         for j in range(i+1,len(s_arr)) :
#             s_arr[j].pop(s_arr[j].index(s_arr[i][0]))
#
#     return answer

def solution(s):
    answer = []

    s1 = s.lstrip('{').rstrip('}').split('},{')
    print(s1)
    new_s = []
    for i in s1:
        new_s.append(i.split(','))

    print(new_s)
    new_s.sort(key = len)

    for i in new_s:
        for j in range(len(i)):
            if int(i[j]) not in answer:
                answer.append(int(i[j]))

    return answer

print(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}"))

text1 = " Hello World Python "
print(text1.lstrip())
print(text1.rstrip())
print(text1.strip())

text2 = "00000Hello World Python000"
print(text2.lstrip('0'))
print(text2.rstrip('0'))
print(text2.strip('0'))

print(text2.lstrip('0Helo'))
print(text2.rstrip('Python0'))
print(text2.strip('0HeloPython'))
