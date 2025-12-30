t = int(input())
for _ in range(t):
    n = int(input())
    arr = [int(input()) for i in range(n)]

    sum_votes = sum(arr)
    max_vote = max(arr)

    half = sum_votes//2+1
    if arr.count(max_vote) == 1 and half <= max_vote:
        print("majority winner", arr.index(max_vote)+1)
    elif arr.count(max_vote) == 1:
        print("minority winner", arr.index(max_vote)+1)
    else:
        print("no winner")
