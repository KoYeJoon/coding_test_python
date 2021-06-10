import itertools

def calc(left,right,op):
    if op=='+':
        return left+right
    elif op == '-':
        return left-right
    else :
        return left*right

def divide_exp_num(expression):
    exp_list = []
    num_list = []
    temp = ''
    for i in range(len(expression)) :
        if not expression[i].isdigit() :
            exp_list.append(expression[i])
            num_list.append(int(temp))
            temp = ''
        else :
            temp += expression[i]

    num_list.append(int(temp))
    return exp_list, num_list

def solution(expression):
    exp_set = set()
    exp_list = []
    num_list = []
    answer = 0
    for i in expression :
        if not i.isdigit() :
            exp_set.add(i)

    prior_exp = list(itertools.permutations(exp_set,len(exp_set)))

    for prior in prior_exp:
        temp = 0
        exp_list, num_list = divide_exp_num(expression)
        for i in prior :
            j=0
            while j<len(exp_list) :
                if exp_list[j] == i :
                    num_list[j] = calc(num_list[j],num_list[j+1],i)
                    num_list.pop(j+1)
                    exp_list.pop(j)
                    j-=1
                j+=1


        answer = max(answer,abs(num_list[0]))
    return answer

print(solution("100-200*300-500+20"))