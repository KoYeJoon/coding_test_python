def solution(weights, head2head):
    boxer_dict = {}
    boxer_num = len(weights)

    for i in range(boxer_num):
        boxer_dict[i+1]=[0,0]
        win_count = 0
        lose_count = 0
        for j in range(boxer_num):
            if head2head[i][j] == 'W':
                win_count += 1
                if weights[i] < weights[j]:
                    boxer_dict[i+1][1] += 1
            elif head2head[i][j] == 'L':
                lose_count += 1

        boxer_dict[i+1][0] = win_count/(win_count+lose_count) if win_count+lose_count>0 else 0

    boxer_item = list(boxer_dict.items())
    boxer_item.sort(key=lambda x : (x[1][0],x[1][1],weights[x[0]-1],-x[0]),reverse=True)

    boxer_list = [i[0] for i in boxer_item]
    return boxer_list

print(solution([50,82,75,120],["NLWL","WNLL","LWNW","WWLN"]))