def solution(inputArray):
     s = max(len(i) for i in inputArray)
     k = [i for i in inputArray if len(i) == s]
     return k
        