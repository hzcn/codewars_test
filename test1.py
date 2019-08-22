numbers = '4 5 29 54 4 0 -214 542 -64 1 -3 6 -6'#字符串
b = numbers.split(' ')#数组
c = []
for n in b:
    c.append(int(n))
#j = str(max(c))
#i = str(min(c))



r = '{} {}'.format(str(max(c)),str(min(c)))
print(r)

