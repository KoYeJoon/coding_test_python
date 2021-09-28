def solution(A, B):
    answer = 0
    A.sort()
    B.sort()
    A_idx = 0
    B_idx = 0
    while A_idx < len(A) and B_idx < len(B):
        if A[A_idx] < B[B_idx] :
            answer += 1
            A_idx += 1
        B_idx += 1

    return answer

print(solution([5,1,3,7],[2,2,6,8]))