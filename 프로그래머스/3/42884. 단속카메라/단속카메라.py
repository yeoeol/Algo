def solution(routes):
    answer = 1
    routes.sort(key=lambda x:x[1])
    # for route in routes:
    #     print(route)
    prev = routes[0][1]
    for i in range(1, len(routes)):
        if routes[i][0] > prev:
            answer += 1
            prev = routes[i][1]

    return answer