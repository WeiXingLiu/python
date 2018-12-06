num1 = 1
haveReachMax = False
while num1 < 6:
    num2 = 1
    value = ''
    while num2 <= num1:
        value += '* '
        num2 += 1
    print(value)
    if num1 == 5:
        haveReachMax = True
    elif num1 == 1 and haveReachMax:
        break
    if haveReachMax:
        num1 -= 1
    else:
        num1 += 1