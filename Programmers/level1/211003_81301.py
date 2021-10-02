# def solution(s):
#     alpha = {'zero':'0','one':'1','two':'2','three':'3','four':'4','five':'5',
#              'six':'6','seven':'7','eight':'8','nine':'9'}
#     alpha_key = list(alpha.keys())
#     temp = ''
#     answer = ''
#     for i in s:
#         if i.isdigit() :
#             if temp != '':
#                 answer += alpha[temp]
#                 temp = ''
#             answer+=i
#         else :
#             temp += i
#             if temp in alpha_key :
#                 answer += alpha[temp]
#                 temp = ''
#
#     return int(answer)
num_dic = {"zero":"0", "one":"1", "two":"2", "three":"3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9"}

def solution(s):
    answer = s
    for key, value in num_dic.items():
        answer = answer.replace(key, value)
    return int(answer)

print(solution("one4seveneight"))