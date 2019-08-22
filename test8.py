x = bin(1234).replace('0b','')

print(x)
total = 0
count = 0
for i in x:
    total = total + int(i)

print(total)