def solution(inputString):
    res = inputString[::-1]
    if inputString == res:
        return True
    else:
        return False
inputString = 'ACCA'
print(solution(inputString))