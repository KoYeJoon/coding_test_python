def give_score(score):
    if score >= 90:
        return 'A'
    if score >= 80:
        return 'B'
    if score >= 70:
        return 'C'
    if score >= 50:
        return 'D'
    return 'F'

def solution(scores):
    answer = ''
    student_num = len(scores)
    for i in range(student_num):
        score_i = []
        for j in range(student_num):
            score_i.append(scores[j][i])

        avg = sum(score_i)/student_num
        if score_i.count(scores[i][i]) == 1 and (scores[i][i]==max(score_i) or scores[i][i]==min(score_i)):
            avg = (sum(score_i) - scores[i][i])/(student_num-1)

        answer += give_score(avg)
    return answer
print(solution([[100,90,98,88,65],[50,45,99,85,77],[47,88,95,80,67],[61,57,100,80,65],[24,90,94,75,65]]))