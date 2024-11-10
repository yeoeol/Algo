from collections import deque

n = int(input())
cards = deque([i for i in range(n, 0, -1)])

while cards:
    print(cards.pop(), end=' ')
    cards.rotate(1)
