def solution(word):
    answer = 0
    vowel = {'A':1,'E':2,'I':3,'O':4,'U':5}
    number = {0:780, 1:155, 2:30, 3:5,4:0}

    new_word = word.rjust(5,'Z')
    idx=0
    while new_word[idx] == 'Z' :
        idx += 1

    for i in range(5-idx) :
        if word[i]=='A' :
            answer += 1
        else :
            answer += (vowel[word[i]]-1)*number[i]+vowel[word[i]]
    return answer

print(solution("AAIE"))