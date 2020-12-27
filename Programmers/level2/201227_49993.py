# def solution(skill, skill_trees):
#     answer = 0
#     for i in skill_trees :
#         temp = [0]*len(skill)
#         j=len(skill)-1
#         tmpTree = i
#         while True:
#             if j==len(skill)-1 and skill[j] in tmpTree :
#                 tmpTree = tmpTree[:tmpTree.index(skill[j])]
#                 temp[j] = 1
#                 j -= 1
#             elif j != len(skill)-1 and 1 in temp[j+1:]:
#                 if skill[j] in tmpTree:
#                     tmpTree = tmpTree[:tmpTree.index(skill[j])]
#                     temp[j] = 1
#                     j -= 1
#                 else :
#                     break
#             else :
#                 if skill[j] in tmpTree:
#                     tmpTree = tmpTree[:tmpTree.index(skill[j])]
#                     temp[j] = 1
#                     j -= 1
#                 else :
#                     j-=1
#             if j==-1:
#                 answer+=1
#                 break
#
#     return answer
def solution(skill, skill_trees):
    answer = 0

    for skills in skill_trees:
        skill_list = list(skill)

        for s in skills:
            if s in skill:
                if s != skill_list.pop(0):
                    break
        else:
            answer += 1

    return answer

print(solution("CBD",["BACDE","CBADF","AECB","BDA"]))