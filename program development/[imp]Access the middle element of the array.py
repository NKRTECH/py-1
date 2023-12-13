n = int(input())
arr = [int(x) for x in input().split()][:n]
if len(arr)%2==0:
    print(arr[len(arr)//2])
else:
    print(arr[(len(arr)-1)//2])