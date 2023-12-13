n = int(input())
arr = [int(x) for x in input().split()][:n]
target = int(input())
for x in arr:
    if x==target:
        print(arr.index(x))
        break
else:
    print('-1')
    
