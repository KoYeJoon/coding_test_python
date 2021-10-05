def solution(sizes):
    min_max=0
    max_max=0
    for size in sizes :
        if max(size)>max_max :
            max_max = max(size)
        if min(size)>min_max:
            min_max = min(size)

    return min_max*max_max

print(solution([[60, 50],[30, 70],[60, 30],[80, 40]]))