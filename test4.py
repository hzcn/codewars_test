arr = range(1,100)
cou = 0
for i in arr:
    cou += 1
#print(sum(arr[0:0]))
#print(sum(arr[1:7]))
#print(sum(arr[0:1]))
#print(sum(arr[2:7]))
#arr[0:1]=0        sum(arr[1:cou]) = 0  #index[0]
#arr[0:n]        sum(arr[2:cou])
#arr[0:3]        sum(arr[3:cou])
#n += 1
n = 0
m = 1

while n < cou:

    if sum(arr[0:n]) == sum(arr[m:cou]):
        print(n)
        break
    else:
        n += 1
        m += 1
if n == cou:
    print(-1)


