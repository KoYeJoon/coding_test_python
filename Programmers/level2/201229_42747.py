def solution(citations):
    citations.sort(reverse=True)
    for i in range(len(citations)):
        if citations[i]<=i :
            return i
    return len(citations)

print(solution([22,24]))

# def solution(citations):
#     citations.sort(reverse=True)
#     answer = max(map(min, enumerate(citations, start=1)))
#     return answer