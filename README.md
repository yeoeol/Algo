# Algo_Python
This is an auto push repository for Baekjoon Online Judge created with [BaekjoonHub](https://github.com/BaekjoonHub/BaekjoonHub).

# 파이썬 알고리즘 기술들
2차원 배열의 행의 합 - 열의 합
```python
for i in range(n):
    gift_score[i] = sum(graph[i]) - sum([k[i] for k in graph])
```
이름 인덱스 매칭
```python
friend = {f: i for i, f in enumerate(friends)}
```
