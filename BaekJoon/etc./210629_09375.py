from sys import stdin

t = int(stdin.readline())

for _ in range(t):
    dict = {}
    n = int(stdin.readline())
    for _ in range(n) :
        value,key = map(str, stdin.readline().split())
        if key not in dict.keys() :
            dict[key]=[value]
        else :
            dict[key].append(value)
    answer = 1
    for key in dict.keys():
        answer *= (len(dict[key])+1)

    print(answer-1)

