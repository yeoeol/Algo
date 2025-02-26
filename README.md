# Algo_Python
This is an auto push repository for Baekjoon Online Judge created with [BaekjoonHub](https://github.com/BaekjoonHub/BaekjoonHub).

# 파이썬 알고리즘 기술들
## 2차원 배열의 행의 합 - 열의 합
```python
for i in range(n):
    gift_score[i] = sum(graph[i]) - sum([k[i] for k in graph])
```
## 이름 인덱스 매칭
```python
friend = {f: i for i, f in enumerate(friends)}
```

범위가 음수를 포함한다면 그 음수만큼 입력받는 값들에 더해줌으로써 인덱스를 양수로 다 바꿈

## 날짜에 대한 문제
num_of_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

