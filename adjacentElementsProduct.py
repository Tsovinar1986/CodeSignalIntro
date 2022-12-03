def solution(inputArray):
    return max(x*y for x,y in zip(inputArray, inputArray[1:]))
print(solution(inputArray = [23,4,-67,89,78,54]))