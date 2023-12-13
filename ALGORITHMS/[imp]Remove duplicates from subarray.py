n = int(input())
arr = [int(x) for x in input().split()]
set1 = set()
for x in arr:
  set1.add(x)
# print(set1)
print(len(set1))