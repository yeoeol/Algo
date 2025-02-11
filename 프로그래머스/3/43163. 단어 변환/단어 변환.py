from collections import deque

def make_graph(words):
    graph = dict()
    for w in words:
        graph[w] = []
    for i in range(len(words)):
        word = words[i]
        for j in range(i+1, len(words)):
            next_word = words[j]
            n = 0
            for k in range(len(words[0])):
                if word[k] == next_word[k]:
                    n += 1
            if n == len(words[0])-1:
                graph[word].append(next_word)
                graph[next_word].append(word)
    return graph

def bfs(graph, start, target):
    queue = deque([(start, 0)])
    visited = [start]
    while queue:
        p, cnt = queue.popleft()
        for w in graph[p]:
            if w == target:
                return cnt+1
            if w not in visited:
                queue.append((w, cnt+1))
                visited.append(w)

def solution(begin, target, words):
    if target not in words:
        return 0

    # 한 글자만 다른 단어끼리 연결해서 그래프 만들기
    words.append(begin)
    graph = make_graph(words)
    answer = bfs(graph, begin, target)

    return answer