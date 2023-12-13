# Given the inputs of three angles a, b and c. Write a program to print "Yes" if these three angles can make a right triangle, otherwise print "No".

# Sample Input:
# 45 100 35

# Sample Output:
# No

# *************method 1************
arr = [int(x) for x in input().split()]
# print(arr)
print('Yes' if any(c==90 for c in arr) and sum(arr)==180 else 'No')

# ***************method 2**************
# arr = [x for x in input().split()]  
# print(arr)
# print('Yes' if any(c=='90' for c in arr) and sum(int(c) for c in arr)==180 else 'No')