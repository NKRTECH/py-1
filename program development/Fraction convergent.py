# Given two integers a and b and where a is divisible by b. It can be represented in the form of a fraction a/b. 
# The task is to reduce the fraction to its lowest form.

# Sample Input: 16 10

# Sample Output: 8 5

# Explanation:

# The lowest fraction that 16/10 can be reduced to is 8/5 and hence 8 5 is the desired output.

# Constraints: 0 < a , b < = 100000

num1,num2 = map(int, input().split())
arr = []
def confrac(num1,num2):
    for i in range(2,min(num1,num2)+1):
        if num1%i==0 and num2%i==0:
            arr.append(i)
    if len(arr)==0:
        print(f'{num1} {num2}')
    else:
        div = max(arr)
        print(f'{num1//div} {num2//div}')
confrac(num1,num2)