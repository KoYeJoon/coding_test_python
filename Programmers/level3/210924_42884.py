# def solution(routes):
#     answer = 0
#     INF = int(1e9)
#     while routes :
#         min_routes = INF
#         max_routes = -30001
#         car_arr = [0]*(60002)
#         for s,d in routes:
#             car_arr[s+30000] += 1
#             car_arr[d+30000] += -1
#             if d > max_routes :
#                 max_routes = d
#             if s < min_routes :
#                 min_routes = s
#
#         min_routes += 30000
#         max_routes += 30000
#         for i in range(min_routes,max_routes+1):
#             car_arr[i] += car_arr[i-1]
#
#         find_index = car_arr.index(max(car_arr))
#         i=0
#         while i < len(routes):
#             if routes[i][0]+30000 <= find_index and routes[i][1]+30000 >= find_index :
#                 routes.pop(i)
#             else :
#                 i+=1
#         answer += 1
#
#     return answer


def solution(routes):
    answer = 0
    while routes :
        routes.sort(reverse=True,key=lambda x : x[1])
        s,d=routes.pop()
        i=0
        while i < len(routes):
            if routes[i][0]<= d and routes[i][1] >= d:
                routes.pop(i)
            else :
                i+=1
        answer += 1

    return answer

print(solution([[-20,15], [-14,-5], [-18,-13], [-5,-3]]))