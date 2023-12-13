# Given an array of integers ‘nums’ and an integer ‘target’, write a program to return indices of the two numbers 
# /such that they add up to target. 
# //You may assume that each input would have exactly one solution, and you may not use the same element twice. 
# //Print -1 when array is empty or when there is no output.

# Sample Input:
# nums = [2,7,11,15], target = 9

# Sample Output:
# 0 1

# Explanation:
# Because nums[0] + nums[1] == 9, we return [0, 1].
def twosum(arr,target):
    arr1 = []
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
          if len(arr1)==0:
            if arr[i] + arr[j] == target:
                arr1.append(i)
                arr1.append(j)
    if len(arr1)==0 :
      print(-1)
    else:
      print(*arr1)


ele = int(input())
arr = [int(x) for x in input().split()]#[:ele]
target = int(input())
twosum(arr,target)