import itertools
def solution(n, weak, dist):
    length = len(weak)
    # 1. weak 배열의 길이를 2배로 늘리기
    for i in range(length):
        weak.append(weak[i]+n)
    # 2. 투입할 친구의 최솟값을 찾기 위해 최댓값보다 1 큰 값으로 초기화
    answer = len(dist)+1
    # 3. 0부터 length-1까지 start 이동하면서 찾기
    for start in range(length):
        for friends in list(itertools.permutations(dist,len(dist))):
            count = 1 # 투입할 친구 수
            # 현재 친구가 점검 가능한 위치 구하기
            position = weak[start]+friends[count-1]
            # 시작점 부터 모든 취약지점 확인
            for i in range(start, start+length):
                if position < weak[i] :
                    count += 1
                    if count > len(dist):
                        break
                    position = weak[i]+friends[count-1]

            answer = min(count,answer)

    if answer > len(dist):
        return -1
    return answer

print(solution(12,[1, 5, 6, 10],[1, 2, 3, 4] ))