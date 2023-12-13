# Powerful digit counts
# The 5-digit number, 16807=75, is also a fifth power. Similarly, the 9-digit number, 134217728=89, is a ninth power.
# Given N, print the N positive integers which are also an Nth power?
# Note: Maximum number of digits will be 10 digits
# Constraint: 1< N< 10
# Sample input: 2
# Sample output:
# 16
# 25
# 36
# 49
# 64
# 81
n = int(input())
arr = []
for i in range(1,11):
    arr.append(i**n)
for x in arr:
    if len(str(x))==n:
        print(x)