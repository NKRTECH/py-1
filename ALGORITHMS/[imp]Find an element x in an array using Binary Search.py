# Write a program that takes an array of integers as input and finds the index of a given element x in the array. 
# If the element exists in the array, the program should return its index. 
# If the element is not found in the array, the program should return -1.
# Sample Input:
# 4 //No. of elements
# 1 2 5 6
# 6 // element to be found
# Output:
# 3
# Explanation:
# The index of element 6 is 3

def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1  # Target element not found
n = int(input())
arr = [int(x) for x in input().split()][:n]
target = int(input())
index = binary_search(arr, target)
print(index if index != -1 else -1)

#**********it is not working for one case**************************
def find_element_index(arr, x):
    for index, value in enumerate(arr):
        if value == x:
            return index
    return -1

n = int(input())
arr = [int(x) for x in input().split()][:n]
target = int(input())

index = find_element_index(arr, target)
print(index)