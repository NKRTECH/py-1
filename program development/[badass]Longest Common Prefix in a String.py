# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

# Sample Input 1:
# [flower, flight, flow]

# Output:
# fl

# Sample Input 2:
# [race, dog, car]

# Output: ""

# arr = [x for x in input().split()]
# arr1 = []
# arr2 = []
# # def toarray(x): 
# #     arr3 = []
# #     for c in arr:
# #         arr3.append(c)
# # for x in range(len(arr)):
# #     # arr1.append((x))    
# # #   print(x[::-1],end=' ')     #this is used to reverse the string
# #     for c in arr[x]:
# # #         arr1.append(c)
# #         arr2.insert(x,list(c))
# # print(arr2)
# # # print(arr1)
# for c in arr:
#     arr1.append(len(c))
# print(arr1)
# num = arr1.index(min(arr1))
# print(arr1.index(min(arr1)))
# def equate(x):
#     for n in x:
#         for i in range(len(num)):

# *********************working code***************************************
# *********************method to input array inside an array****************

# r = int(input())
# arr = []
# for i in range(r):
#     arr.append([j for j in input()]) #if input().split() then it will not separate each letter in word
# print(arr)

# # **************************************************
# arr1 = []
# prefix = ''
# for c in arr:
#     arr1.append(len(c))
# print(arr1)
# num = arr1.index(min(arr1))
# print(num)
# for x in range(1,len(arr)):
#     for y in range(len(arr[num])):
#         if arr[x-1][y]==arr[x][y]:
#             prefix+=arr[x][y]
#     else:
#         break
# print(prefix)

# ********************Working code*********************

# arr = [x for x in input().split()]
# arr1 = []
# prefix = ''
# for c in arr:
#     arr1.append(len(c))
# num = arr1.index(min(arr1))
# for y in range(1,len(arr)):
#     for c in range(len(arr[num])):
#         if all(arr[y-1][c]==arr[y][c]):
#             prefix+=arr[y-1][c]
#             # if prefix==arr[y][c]:
#             #     print
            
#         else:
#             break
#     # break
# print(prefix)

# n = int(input())
# arr = [x for x in input().split()]
# # arr.sort()
# # print(arr)
# arr1 = []
# prefix = ''
# conflict = ''
# for c in arr:
#     arr1.append(len(c))
# num = arr1.index(min(arr1))
# for y in range(1,len(arr)):
#     for c in range(len(arr[num])):
#         if arr[y-1][c]==arr[y][c]:
#             prefix+=arr[y][c]
#         else:
#             conflict+=arr[y][c]
            
#     # break
# print(prefix)
# print(conflict)
# for j in arr:
#     if j in conflict:
#         print('""')   
#     else:
#         print(prefix)
# ****************livebook solution*******************
#Function to return the longest common prefix
# def longest_common_prefix(arr,n):
#     #sorting the array of strings
#     arr.sort()

#     #storing the first string of the array
#     s1=arr[0]
#     #storing the last string of the array
#     s2=arr[n-1]

#     #Initializing an empty string for answer
#     ans=""
#     i=0

#     #Iterate the loop till i remains lesser than length of the first and the last string
#     while(i<len(s1) and i<len(s2)):
#         #Compare and if we found same character add it to the prefix storing var i.e ans
#         if(s1[i]==s2[i]):
#             ans+=s1[i]
#         else:
#             break
#         #Increment i
#         i+=1
    
#     #returning the longest common prefix
#     return ans
    
# #Taking Integer Input n
# n=int(input())

# #Taking elements Input of array
# arr=[i for i in input().split()]

# #Printing the longest common prefix by calling the function
# print(longest_common_prefix(arr,n))

# *************AI Generated Code**************
# def longest_common_prefix(strs):
#   """Finds the longest common prefix string amongst an array of strings.

#   Args:
#     strs: A list of strings.

#   Returns:
#     A string, the longest common prefix of all the strings in the array, or an empty
#     string if there is no common prefix.
#   """

#   if not strs:
#     return ""

#   # Sort the array of strings in alphabetical order.
#   strs.sort()

#   # Initialize the longest common prefix.
#   longest_common_prefix = ""

#   # Iterate over the characters in the first string.
#   for i in range(len(strs[0])):
#     # Check if the current character is the same in all strings in the array.
#     if all(strs[0][i] == s[i] for s in strs[1:]):
#       # Append the character to the longest common prefix.
#       longest_common_prefix += strs[0][i]
#     else:
#       # We have reached the end of the longest common prefix.
#       break

#   return longest_common_prefix

# arr = [x for x in input().split()]
# print(longest_common_prefix(arr))

# *****************AI Generated Code**************
def longestCommonPrefix(strs):
    if not strs:
        return ""
    prefix = strs[0]
    for i in range(1, len(strs)):
        while strs[i].find(prefix) != 0:
            prefix = prefix[:-1]
            if not prefix:
                return ""
    return prefix
arr = [x for x in input().split()]
print(longestCommonPrefix(arr))