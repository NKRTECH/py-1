# Write a program to print the first reduced form of a given fraction. 
# The two number Inputs denote the numerator and denominator respectively. 
# If there is no reduced form possible then print the original Input fraction.

# Sample Input: 4 16
# Sample Output: 2/8

# Explanation: The fraction 4/16 can be reduced to 2/8 and then to 1/4. 
# The first reduced form is 2/8 and hence this is the output.

num1,num2 = input().split()
num1 = int(num1)
num2 = int(num2)
arr = []
for i in range(2,min(num1,num2)+1):
    if num1%i==0 and num2%i==0:
        arr.append(i)

if len(arr)==0:
    print(f'{num1}/{num2}')
else:
    div = min(arr)
    print(f'{num1//div}/{num2//div}')


