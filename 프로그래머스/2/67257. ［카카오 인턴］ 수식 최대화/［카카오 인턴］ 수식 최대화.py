import itertools
import re

def solution(expression):
    operands = re.split(r'(\D)', expression)
    original_operands = operands.copy()
    operator = list(itertools.permutations(['*', '-', '+']))
    M = 0
    for k in operator:
        for op in k:
            while op in operands:
                idx = operands.index(op)
                a = int(operands[idx-1])
                b = int(operands[idx+1])
                if op == '*':
                    result = a*b
                elif op == '-':
                    result = a-b
                else:
                    result = a+b
                for _ in range(3):
                    operands.pop(idx-1)
                operands.insert(idx-1, result)
        M = max(M, abs(int(operands[0])))
        operands = original_operands.copy()
    return M