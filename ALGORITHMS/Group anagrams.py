n = int(input())
arr = [list(x) for x in input().split()][:n]
arr1 = []
arr2 = []
for x in arr:
    x.sort()
    arr2.append(arr.count(x))
print(*arr)
for index,value in enumerate(arr):
    arr1.append(index)
print(*arr1)