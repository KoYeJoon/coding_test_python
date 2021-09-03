from collections import deque

def solution(tickets):
    answer = deque()
    ticket_dict = {}

    for s,d in tickets :
        if s not in ticket_dict.keys():
            ticket_dict[s] = [d]
        else:
            ticket_dict[s].append(d)

    keys = ticket_dict.keys()
    for i in keys:
        ticket_dict[i].sort(reverse=True)

    stack = ['ICN']
    while stack:
        dt = stack[-1]
        if dt not in keys :
            answer.appendleft(stack.pop())
        elif not ticket_dict[dt]:
            answer.appendleft(stack.pop())
        else :
            stack.append(ticket_dict[dt].pop())


    return list(answer)

print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]]))
# 2, 0,1