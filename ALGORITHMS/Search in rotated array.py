n = int(input())
arr = [int(x) for x in input().split()]
target = int(input())
print(arr.index(target) if target in arr else -1)