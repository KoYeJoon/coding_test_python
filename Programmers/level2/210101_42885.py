# def solution(people, limit):
#     answer = 0
#     people.sort(reverse=True)
#     while len(people)>0:
#         if len(people)==1 :
#             people.pop(0)
#         elif people[0]+people[-1] > limit:
#             people.pop(0)
#         else :
#             for j in range(1,len(people)-1):
#                 if people[0]+people[j] <= limit :
#                     people.pop(j)
#                     people.pop(0)
#                     break
#
#         answer += 1
#
#     return answer

def solution(people, limit):
    answer = 0
    people.sort(reverse=True)
    i=0
    j=len(people)-1
    while i<j :
        if people[i] + people[j] <= limit :
            j-=1
            answer+=1
        i+=1
    return len(people)-answer

print(solution([70, 80, 50],100))