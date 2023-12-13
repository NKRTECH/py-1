# Write a program to check whether the given number is an Armstrong number or not. 
# An n-digit number that is the sum of the nth powers of its digits is called an n-narcissistic number.
# It is also sometimes known as an Armstrong number.
# Sample input: 371

# Sample Output: Armstrong number

# Explanation: 3x3x3 + 7x7x7 + 1x1x1 = 371

num = input()
arr = []
for c in num:
    arr.append(int(c)**len(num))
if sum(arr)==int(num):
    print('Armstrong number')
else:
    print('Not an armstrong number')