def phase_2(id):
    available_id = ['-','_','.']
    answer = ''
    for i in id:
        if i.isdigit() or i.isalpha() or i in available_id :
            answer += i
    return answer

def phase_3(id):
    answer = ''
    dot_flag = 0
    for i in id :
        if i == '.':
            if not dot_flag :
                answer += i
                dot_flag = 1
        else :
            answer += i
            dot_flag = 0
    return answer

def phase_4_6(id):
    if len(id)>0 and id[0] == '.':
        id = id[1:]
    if len(id)>0 and id[-1] == '.':
        id = id[:-1]
    return id

def solution(new_id):
    # 1단계
    new_id = new_id.lower()

    # 2단계
    new_id = phase_2(new_id)

    # 3단계
    new_id = phase_3(new_id)

    # 4단계
    new_id = phase_4_6(new_id)

    # 5단계
    if len(new_id)==0 :
        new_id += 'a'

    # 6단계
    if len(new_id)>15 :
        new_id = phase_4_6(new_id[:15])

    # 7단계
    if len(new_id)<3 :
        for i in range(3-len(new_id)):
            new_id+=new_id[-1]

    return new_id