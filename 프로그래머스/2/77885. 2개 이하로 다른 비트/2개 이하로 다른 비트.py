def solution(numbers):
    can = []
    for num in numbers:
        bin_num = list(bin(num)[2:])
        for i in range(len(bin_num)-1, -1, -1):
            if bin_num[i] == '0':
                bin_num[i] = '1'
                if i+1 < len(bin_num):
                    bin_num[i+1] = '0'
                can.append(int(''.join(bin_num), 2))
                break
        else:
            can.append(int(''.join(['1', '0'] + bin_num[1:]), 2))
    return can