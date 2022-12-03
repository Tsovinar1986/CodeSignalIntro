def solution(inputString):
    mylist1 = list(inputString)
    open_bracket_indexes = []
    for i, character in enumerate(mylist1):
        if character == '(':
            open_bracket_indexes.append(i)
        elif character == ')':
            j = open_bracket_indexes.pop()
            mylist1[j:i] = mylist1[i:j:-1]
    return ''.join(character for character in mylist1 if character not in '()')
