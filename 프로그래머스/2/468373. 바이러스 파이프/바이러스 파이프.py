from itertools import product
import copy

def dfs(p_num, infection_list, edges):
    stack = copy.deepcopy(infection_list)
    #print(f"stack:{stack}")
    while stack:
        x = stack.pop()
        for s, e, p in edges:
            if s == x and p == p_num and e not in infection_list:
                infection_list.append(e)
                stack.append(e)
    return infection_list


def solution(n, infection, edges, k):
    m = len(edges)
    for i in range(m):
        s, e, p = edges[i]
        edges.append([e, s, p])
    answer = 0
    for pipe_ord in product([1,2,3], repeat=k):
        infection_list = [infection]
        for p_num in pipe_ord:
            infection_list = dfs(p_num, infection_list, edges)
            #print(pipe_ord, p_num, infection_list)
        answer = max(answer, len(infection_list))

    return answer
