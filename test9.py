arr = [0,1,2,3,4,5,6,7,8,9]
max = 0
for i in range(len(arr)):
    for j in range(len(arr)+1):
        s = sum(arr[i:j])
        if s > max:
            max = s
print(max)
