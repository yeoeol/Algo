from math import ceil
import sys

def input():
    return sys.stdin.readline().strip()

def fight(arr, max_hp, atk):
    cur_hp = max_hp
    for t, a, h in arr:
        if t == 2:
            atk += a
            cur_hp = min(max_hp, cur_hp+h)
        else:
            war_to_monster = ceil(h / atk)
            cur_hp -= (war_to_monster-1)*a
            if cur_hp <= 0:
                return False
    return True

def bin_search(arr, atk):
    left, right = 1, 10**12 * n
    while left <= right:
        mid = (left+right)//2
        if fight(arr, mid, atk):
            right = mid-1
        else:
            left = mid+1
    return left


n, atk = map(int, input().split())
arr = [tuple(map(int, input().split())) for _ in range(n)]
print(bin_search(arr, atk))
