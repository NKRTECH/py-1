n = int(input())
arr = [int(x) for x in input().split()]
target = int(input())
count = arr.count(target)
if target in arr:
    print(*[arr.index(target),arr.index(target)+count-1])
else:
    print(*[-1,-1])