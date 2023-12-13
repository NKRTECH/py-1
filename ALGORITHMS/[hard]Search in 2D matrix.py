rows = int(input())
columns = int(input())
arr = []
count = 0
for i in range(rows):
    arr.append([int(x) for x in input().split()][:columns])
target = int(input())

#**************************METHOD 1**************************
for x in arr:
    if target in x:
      count+=1
if count >0:
  print('True')
else:
  print('False')

#**************************METHOD 2**************************
if any(target in x for x in arr):
    print('True')
else:
    print('False')