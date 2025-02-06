def solution(storey):
    answer = 0

    while storey:
        remainder = storey % 10

        if remainder > 5:
            answer += 10-remainder
            storey += 10
        elif remainder == 5:
            if (storey//10)%10 >= 5:
                storey += 10
            answer += remainder
        else:
            answer += remainder

        storey //= 10

    return answer