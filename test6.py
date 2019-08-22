#seven(times(five())), 35
#seven = 7
#times = *
#five = 5
#7 * 5 = 35
def seven(a='7'):
    if a != '7':
        if a[0] == '+':
            return 7+int(a[1])
        if a[0] == '-':
            return 7-int(a[1])
        if a[0] == '*':
            return 7*int(a[1])
        if a[0] == '/':
            return int(7/int(a[1]))
    else:
        return '7'
def five(a='5'):
    if a != '5':
        if a[0] == '+':
            return 5+int(a[1])
        if a[0] == '-':
            return 5-int(a[1])
        if a[0] == '*':
            return 5*int(a[1])
        if a[0] == '/':
            return int(5/int(a[1]))
    else:
        return '5'

def times(a):
    return '*'+a

print(seven(times(five())))