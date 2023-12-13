# Given an array of N integers, your task is to find unique triplets that add up to give a sum of zero. 
# So, you need to return an array of all the unique triplets [arr[a], arr[b], arr[c]] 
# such that i!=j, j!=k, k!=i, and their sum is equal to zero.

# Input: n = 6 nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]

#*******************My written code************************
n = int(input())
arr = [int(x) for x in input().split()]
arr1 = []
arr2 =[]
set1 = set()
for i in range(len(arr)):
    for j in range(i+1, len(arr)):
        for k in range(j+1, len(arr)):
            if arr[i]+arr[j]+arr[k] == 0:
                arr1.append([arr[i],arr[j],arr[k]])
for x in arr1:
  x.sort()
for x in arr1:
  set1.add(tuple(x))
for x in set1:
  arr2.append(list(x))
#   arr2.reverse()
# print(arr2)
if len(arr1)==0:
  print('No triplet found')
else:
  for c in arr2:
    print(*c)

#*********************AI Generated Code***********************
n = int(input())
arr = [int(x) for x in input().split()]
arr1 = []
for i in range(len(arr)):
    for j in range(i+1, len(arr)):
        for k in range(j+1, len(arr)):
            if arr[i] + arr[j] + arr[k] == 0:
                arr1.append([arr[i], arr[j], arr[k]])

# Remove duplicates
unique_triplets = []
for triplet in arr1:
    triplet.sort()
    if triplet not in unique_triplets:
        unique_triplets.append(triplet)
        # unique_triplets.reverse()

if len(unique_triplets) == 0 :
    print('No triplet found')
else:
    for triplet in unique_triplets:
        print(*triplet)