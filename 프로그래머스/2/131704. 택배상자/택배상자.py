def solution(order):
    belt = list(reversed(range(1, len(order)+1)))
    second_belt = []

    ans = 0
    for target in order:
        while True:
            if second_belt and second_belt[-1] == target:
                second_belt.pop()
                ans += 1
                break
            if belt:
                if belt[-1] == target:
                    belt.pop()
                    ans += 1
                    break
                else:
                    second_belt.append(belt.pop())
            else:
                return ans
    return ans
