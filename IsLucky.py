def solution(n):
    n = str(n)
    first_half = sum([int(i) for i in list(n[0: int(len(n)/ 2)])])
    second_half = sum([int(i) for i in list(n[int(len(n)/ 2): len(n)])])
    return first_half == second_half