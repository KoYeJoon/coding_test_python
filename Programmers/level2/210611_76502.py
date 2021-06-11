def correct(s):
    st = list(s)[::-1]
    open_s = ['(','{','[']
    temp = []

    while len(st) > 0:
        st_pop = st.pop()
        if st_pop in open_s :
            temp.append(st_pop)
        else :
            if len(temp)<1 :
                return False
            temp_pop = temp.pop()
            if temp_pop == '(' and st_pop != ')' :
                return False
            elif temp_pop == '{' and st_pop != '}' :
                return False
            elif temp_pop == '[' and st_pop != ']':
                return False

    if len(temp) > 0:
        return False
    return True

def solution(s):
    answer = 0
    for i in range(len(s)):
        temp_s = s[i:] + s[:i]
        if correct(temp_s):
            answer += 1
    return answer

print(solution("[](){}"))