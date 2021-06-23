def solution(enroll, referral, seller, amount):
    answer = []
    dicts = {}
    tree_dicts = {}
    for i in range(len(enroll)):
        tree_dicts[enroll[i]] = referral[i]
        dicts[enroll[i]] = 0

    for i in range(len(seller)) :
        cost = amount[i]*100
        node = seller[i]
        while node != '-':
            parent = tree_dicts[node]
            if cost*0.1 < 1:
                dicts[node] += cost
                break
            dicts[node] += (cost-(cost//10))
            cost //= 10
            node = parent


    for name in enroll :
        answer.append(int(dicts[name]))
    return answer

print(solution(["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"],
               ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"],
               ["young", "john", "tod", "emily", "mary"],
               [12, 4, 2, 5, 10]))