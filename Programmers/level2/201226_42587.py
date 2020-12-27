def solution(priorities, location):
    temp = list(range(0,len(priorities)))
    print_seq = []
    while True :
        prior = priorities.pop(0)
        num = temp.pop(0)
        for j in range(len(priorities)) :
            if prior < priorities[j] :
                priorities.append(prior)
                temp.append(num)
                break
            if j == len(priorities)-1 :
                print_seq.append(num)
        if len(priorities)==0 :
            print_seq.append(num)
            break

    return print_seq.index(location)+1

print(solution([2, 1, 3, 2],2))