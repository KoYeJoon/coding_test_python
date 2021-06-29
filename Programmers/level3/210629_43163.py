def difference_num(a1, a2) :
    differ = 0
    for i in range(len(a1)) :
        if a1[i] != a2[i] :
            differ += 1

    return differ

def solution(begin, target, words):
    if target not in words :
        return 0

    answer = int(1e9)
    count = 0
    stack = []
    visited = [False] * len(words)
    stack.append(begin)
    while stack :
        word = stack.pop()
        if word == target :
            if count < answer :
                answer = count
                count = 0
        else :
            for i in range(len(words)) :
                if difference_num(words[i],word) == 1 and not visited[i]:
                    stack.append(words[i])
                    visited[i]=True
        count += 1



    return answer

print(solution("hit","cog",["hot", "dot", "dog", "lot", "log", "cog"]	))