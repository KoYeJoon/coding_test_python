def check(pos_x,pos_y):
    if pos_x<0 or pos_x>10 or pos_y<0 or pos_y>10 :
        return False
    return True

def solution(dirs):
    count = 0
    visited = []
    pos_x = 5
    pos_y = 5

    for dir in dirs :
        new_x, new_y = pos_x, pos_y

        if dir == 'U':
            new_x -= 1
        elif dir == 'D':
            new_x += 1
        elif dir == 'R':
            new_y += 1
        else :
            new_y -= 1

        if check(new_x,new_y):
            if [[pos_x,pos_y],[new_x,new_y]] not in visited:
                visited.append([[pos_x,pos_y],[new_x,new_y]])
                visited.append([[new_x,new_y],[pos_x,pos_y]])
                count += 1
            pos_x , pos_y = new_x, new_y

    return count


print(solution("ULURRDLLU"))