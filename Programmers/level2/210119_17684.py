def solution(msg):
    answer = []
    # dic_msg = dict(zip(range(1,27),"ABCDEFGHIJKLMNOPQRSTUVWXYZ"))
    # dic_msg = {1:'A',2:'B',3:'C',4:'D',5:'E',6:'F',
    #            7:'G',8:'H',9:'I',10:'J',11:'K',12:'L',
    #            13:'M',14:'N',15:'O',16:'P',17:'Q',18:'R',
    #            19:'S',20:'T',21:'U',22:'V',23:'W',24:'X',
    #            25:'Y',26:'Z'}
    while True:
        w=''
        c= ''
        count = 0
        while count < len(msg):
            w += msg[count]
            for num,alp in dic_msg.items():
                if alp == w:
                    break
            else :
                w = w[:-1]
                c=msg[count]
                dic_msg[len(dic_msg)+1] = w+c
                break
            count += 1
        for num,alp in dic_msg.items():
            if alp == w:
                answer.append(num)
                break
        if c == '':
            break
        msg = msg[len(w):]

    return answer

print(solution('KAKAO'))