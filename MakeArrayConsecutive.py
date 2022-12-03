def solution(statues):
    sortl = sorted(statues)
    smallist = sortl[0]
    biggiest = sortl[-1]
    return (biggiest - smallist -1) - len(statues) + 2