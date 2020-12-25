def solution(numbers, hand):
    answer = ''
    left = [1,4,7]
    right= [3,6,9]

    # [0,1,2,3,4,5,6,7,8,9,*,#]
    center_2 = [3,1,0,1,2,1,2,3,2,3,4,4]
    center_5 = [2,2,1,2,1,0,1,2,1,2,3,3]
    center_8 = [1,3,2,3,2,1,2,1,0,1,2,2]
    center_0 = [0,4,3,4,3,2,3,2,1,2,1,1]
    left_pos = 10
    right_pos= 11

    #거리가 같으면 왼손잡이면 왼손, 오른손잡이면 오른손!
    for i in numbers :
        if i in left :
            left_pos = i
            answer += 'L'
        elif i in right :
            right_pos = i
            answer += 'R'
        else :
            if i == 2 :
                if center_2[left_pos] > center_2[right_pos] :
                    answer += 'R'
                    right_pos = 2
                elif center_2[left_pos] < center_2[right_pos] :
                    answer += 'L'
                    left_pos = 2
                else :
                    if hand == 'left' :
                        answer += 'L'
                        left_pos = 2
                    else :
                        answer += 'R'
                        right_pos = 2

            elif i == 5 :
                if center_5[left_pos] > center_5[right_pos] :
                    answer += 'R'
                    right_pos = 5
                elif center_5[left_pos] < center_5[right_pos] :
                    answer += 'L'
                    left_pos = 5
                else :
                    if hand == 'left' :
                        answer += 'L'
                        left_pos = 5
                    else :
                        answer += 'R'
                        right_pos = 5
            elif i == 8 :
                if center_8[left_pos] > center_8[right_pos] :
                    answer += 'R'
                    right_pos = 8
                elif center_8[left_pos] < center_8[right_pos] :
                    answer += 'L'
                    left_pos = 8
                else :
                    if hand == 'left' :
                        answer += 'L'
                        left_pos = 8
                    else :
                        answer += 'R'
                        right_pos = 8
            else :
                if center_0[left_pos] > center_0[right_pos] :
                    answer += 'R'
                    right_pos = 0
                elif center_0[left_pos] < center_0[right_pos] :
                    answer += 'L'
                    left_pos = 0
                else :
                    if hand == 'left' :
                        answer += 'L'
                        left_pos = 0
                    else :
                        answer += 'R'
                        right_pos = 0

    return answer

print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5],"right"))