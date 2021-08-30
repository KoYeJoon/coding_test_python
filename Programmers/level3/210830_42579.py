def solution(genres, plays):
    answer = []
    dict_genre = {}
    dict_sum = {}
    for i in range(len(genres)):
        if genres[i] in dict_genre :
            dict_genre[genres[i]].append([plays[i],i])
            dict_sum[genres[i]] += plays[i]
        else:
            dict_genre[genres[i]] = [[plays[i],i]]
            dict_sum[genres[i]] = plays[i]

    keys = sorted(dict_genre.keys(),key = lambda x : dict_sum[x], reverse=True)

    for k in keys:
        dict_genre[k].sort(key = lambda x : (-x[0], x[1]))
        for i in range(min(2,len(dict_genre[k]))):
            answer.append(dict_genre[k][i][1])
    return answer

print(solution(["classic", "pop", "classic", "classic", "pop"],[500, 600, 150, 800, 2500]))