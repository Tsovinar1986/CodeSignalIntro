def solution(a):
       b = 0
       k = sorted([i for i in a if i != -1])
       for j in range(len(a)):
        if a[j] != -1:
          a[j] = k[b]
          b += 1
       return a