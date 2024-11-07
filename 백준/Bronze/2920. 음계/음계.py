nums = list(map(int, input().split()))
ans = [1,2,3,4,5,6,7,8]
rev_ans = list(reversed(ans))

if nums == ans:
    print("ascending")
elif nums == rev_ans:
    print("descending")
else:
    print("mixed")