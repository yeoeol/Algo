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

## 어떤 수열에서 조건에 맞는 값들만 리스트로 만들고 싶을 때
```python
arr = [1, 3, 3, 0, 0, 2, 1, 3]
arr = list(filter(lambda x: x > 0, arr))
```

## row1, row2 행에 대해 같은 열에 같은 숫자를 갖는 경우가 있는지를 찾아줌
- 즉 2차원 배열의 두 열에 대해서, 행 별로 비교
```python
def has_same_number(row1, row2):
    return any([
        a[row1][col] == a[row2][col]
        for col in range(1, m + 1)
    ])
```
