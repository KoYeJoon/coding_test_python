import collections
def solution(cacheSize, cities):
    answer = 0
    cache = collections.deque()
    if cacheSize == 0:
        return len(cities)*5
    for i in range(len(cities)):
        if len(cache) < cacheSize :
            if cities[i].lower() in cache :
                cache.remove(cities[i].lower())
                answer += 1
            else :
                answer += 5
            cache.appendleft(cities[i].lower())
        else :
            if cities[i].lower() in cache :
                cache.remove(cities[i].lower())
                answer += 1
            else :
                cache.pop()
                answer += 5
            cache.appendleft(cities[i].lower())
    return answer

print(solution(2,['Jeju', 'Pangyo', 'NewYork', 'newyork']))