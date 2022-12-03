from collections import Counter

def solution(s1, s2):
    k = Counter(s1)
    r = Counter(s2)
    count =0
    s = set()
    for i in s1:
        if i in r and i not in s:
            count += r[i] if k[i] > r[i] else k[i]
            s.add(i)
    return count
