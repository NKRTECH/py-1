# Given two Input numbers a and b representing a/b where a < b. Write a program to print all the reduced forms of the given fraction a/b in a single line. Print -1 if the Input is already in the most reduced fraction.

# Sample Input: 6 12

# Sample Output: 3/6 2/4 1/2

# Explanation:

# 3/6, 2/4, and 1/2 are all the possible reduced forms of the given fraction which is 6/12.

# *********************without defining function****************
# num1,num2 = input().split()
# num1 = int(num1)
# num2 = int(num2)
# arr = []
# for i in range(2,min(num1,num2)+1):
#     if num1%i==0 and num2%i==0:
#         arr.append(i)
# if len(arr)==0:
#     print(-1)
# else:
#     for x in arr:
#         print(f'{num1//x}/{num2//x}',end=' ')

#****************better solve with defining function we can call it anywhere****************
arr = []
def reqfraction(num1,num2):
    for i in range(2,min(num1,num2)+1):
        if num1%i==0 and num2%i==0:
            arr.append(i)
    if len(arr)==0:
        print(-1)
    else:
        for x in arr:
            print(f'{num1//x}/{num2//x}',end=' ')
# num1,num2 = input().split()
# num1 = int(num1)
# num2 = int(num2)
num1,num2=map(int, input().split())
reqfraction(num1,num2)