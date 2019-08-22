def maxSequence(arr):
    max,curr=0,0
    for x in arr:
        curr+=x
        if curr<0:curr=0
        if curr>max:max=curr
    return max
arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(maxSequence(arr))