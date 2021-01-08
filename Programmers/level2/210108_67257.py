import itertools
def solution(expression):
    exp_set = set()
    for i in expression :
        if not i.isdigit() :
            exp_set.add(i)
    exp_list = list(itertools.permutations(exp_set,len(exp_set)))
    answer = 0
    for i in exp_list :
        expression_list = list(expression)
        for j in i :
            k=0
            while k<len(expression_list):
                if expression_list[k]==j :
                    temp = []
                    for a in range(k-1,-1,-1) :
                        if expression_list[a] in i :
                            if a != 0 and expression_list[a-1] == '(' :
                                temp.append(a-1)
                            else :
                                temp.append(a+1)
                            break
                        if a == 0:
                            temp.append(0)
                    for a in range(k+1,len(expression_list)):
                        if expression_list[a] in i :
                            if expression_list[a-1] == '(':
                                continue
                            else :
                                temp.append(a)
                                break
                        if a==len(expression_list)-1 :
                            temp.append(len(expression_list))
                    temp_ans = '('+str(eval(''.join(expression_list[temp[0]:temp[1]])))+')'
                    expression_list = expression_list[:temp[0]]+list(temp_ans)+ expression_list[temp[1]:]
                    k=temp[0]+len(temp_ans)-1
                k+=1
        str_exp = ''.join(expression_list[1:-1])
        if answer < abs(int(str_exp)) :
            answer =abs(int(str_exp))


    return answer


print(solution("100-200*300-500+20"))