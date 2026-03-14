def solution(numbers):
    can = []
    for num in numbers:
        bin_num = list(bin(num)[2:])
        for i in range(len(bin_num)-1, -1, -1):
            if bin_num[i] == '0':
                bin_num[i] = '1'
                if i+1 < len(bin_num):
                    bin_num[i+1] = '0'
                can.append(bin_num)
                break
        else:
            can.append(['1', '0'] + bin_num[1:])
    ans = []
    for lst in can:
        ans.append(int(''.join(lst), 2))
    return ans