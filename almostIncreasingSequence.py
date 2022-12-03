def solution(sequence):
      if len(sequence) == 1:
        return False
      if len(sequence) == 2:
        return True
      c = 0
      c1 = 0
      for i in range(1,len(sequence)):
        if sequence[i-1] >= sequence[i]:
            c += 1
        if i != 0 and i+1 < len(sequence):
            if sequence[i-1] >= sequence[i+1]:
                c1 += 1
        if c > 1 or c1 > 1:
            return False
      return c1 == 1 or c == 1