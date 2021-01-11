def solution(n, words):
    answer = [0,0]
    turn = 1
    temp = words[0][-1]
    word_temp=[words[0]]
    while turn < len(words) :
        if temp != words[turn][0] or words[turn] in word_temp :
            answer[0] = turn%n + 1
            answer[1] = turn // n + 1
            break
        word_temp.append(words[turn])
        temp = words[turn][-1]
        turn += 1
    return answer

print(solution(	["tank","kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]))