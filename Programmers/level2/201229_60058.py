def good_str(p):
    left = 0
    right = 0

    for i in range(len(p)):
        if p[i]=='(':
            left+=1
        else :
            right += 1
        if left<right:
            return False
    return True

def solution(p):
    left = 0
    right = 0
    answer=''
    if good_str(p) :
        return p
    else :
        mark = 0
        if p[0]==')':
            mark = 1
        for i in range(len(p)) :
            if p[i] == '(' :
                left += 1
            else :
                right +=1

            print(left,right,mark)
            # 좌항보다 우항이 더 많은 경우, 균형잡히지 않음
            if mark==0 and right != 0 and left < right :
                u = p[:i]
                v = p[i:]
                if good_str(u):
                    answer += u +solution(v)
                else :
                    temp_u = u[1:-1]
                    answer += '(' + solution(v) + ')'
                    for i in temp_u :
                        if i== '(' :
                            answer += ')'
                        else :
                            answer += '('
                return answer

            if mark==1 and left != 0 and right<=left :
                u = p[:i+1]
                v = p[i+1:]
                if good_str(u):
                    answer += u +solution(v)
                else :
                    temp_u = u[1:-1]
                    answer += '(' + solution(v) + ')'
                    for i in temp_u :
                        if i== '(' :
                            answer += ')'
                        else :
                            answer += '('
                return answer


        return answer

print(solution(")()()()("))