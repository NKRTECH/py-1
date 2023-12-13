# Given an integer array arr, find the subarray which has the largest sum and return its sum.

# Example:

# Sample Input:
# 9
# -2 -1 -3 4 -1 2 1 -5 4

# Output: 6

n = int(input())
arr = [int(x) for x in input().split()]
arr1 = []
arr2 = []
for i in range(len(arr)):
  for j in range(i,len(arr)):
    arr1.append(arr[i:j+1])
# print(arr1)
for x in arr1:
  arr2.append(sum(x))
# print(arr2)
if arr1==[]:
  print(0)
else:
    print(max(arr2))
# print(arr1[arr2.index(max(arr2))])




# n = int(input())
# arr = [int(x) for x in input().split()][:n]
# arr1 = []
# arr2 = []
# required = int(input())
# for x in arr:
#     if x>0:
#         arr1.append(x)
# print(*arr1)
# for x in arr:
#     if x>0:
#         arr2.append(arr.index(x))
# print(*arr2)