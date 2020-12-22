def solution(participant, completion):
    for i in participant :
        if i in completion :
            completion.remove(i)
        elif i not in completion :
            return i


def solution(participant, completion):
    participant.sort()
    completion.sort()
    for i in range(len(completion)):
        if participant[i]!=completion[i]:
            return participant[i]
    return participant[len(participant)-1]


import collections

def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]


print(solution(["mislav","stanko","mislav","ana"],["stanko","ana","mislav"]))