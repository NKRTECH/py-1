# Print the longest string of the list
# Given an array of string, write a program to print the longest string.

# Example:
# Input:
# 5
# apple orange lemon fruits bananas

# Output:
# bananas

n= int(input())
arr = [x for x in input().split()][:n]
arr1 = []
for c in arr:
    arr1.append(len(c))
mx = max(arr1)
print(arr[arr1.index(mx)])
