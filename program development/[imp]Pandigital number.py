# An n-digit number is pandigital if it uses all the digits 1 to n exactly once; 
# for example, the 5-digit number, 15234, is 1 through 5 pandigital. 
# You are given an input number, print "Yes" if it is a pandigital number else print "No".

# Sample Input: 54321

# Sample Output: Yes
# *************method 1************
num = [int(x) for x in input()]
if any(j not in num for j in range(1,int(max(num)))):
    print('No')
else:
    print('No' if any(num.count(c) > 1 for c in num) else 'Yes')

# *************method 2************
num = [int(x) for x in input()]
num.sort()
for j in range(1,int(max(num))):
    if j not in num:
        print('No')
        break
else:          #*****listen this else keyword is also a part of for loop so the break statement in if condition completely stopped the for loop
    print('No' if any(num.count(c) > 1 for c in num) else 'Yes')



