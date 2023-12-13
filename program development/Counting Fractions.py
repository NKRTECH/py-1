# Given two Input numbers a and b representing a/b where a < b. 
# Write a program to print the total count of all reduced forms of the given fraction a/b.

# Sample Input: 6 12

# Sample Output: 3

# Explanation:

# The three lowest possible forms are 3/6, 2/4, and 1/2 and hence the answer would be 3.

arr = []
def countfrac(num1,num2):
    for i in range(2,min(num1,num2)+1):
        if num1%i==0 and num2%i==0:
            arr.append(i)
    if len(arr)==0:
        return 0
    else:
        return len(arr)
num1,num2 = map(int, input().split())
print(countfrac(num1,num2))