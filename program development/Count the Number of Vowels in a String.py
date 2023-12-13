# **************Method 1***************
# char = input()
# count  = 0
# for c in char:
#     if c=='a' or c=='A':
#         count+=1
#     elif c=='e' or c=='E':
#         count+=1
#     elif c=='i' or c=='I':
#         count+=1
#     elif c=='o' or c=='O':
#         count+=1
#     elif c=='u' or c=='U':
#         count+=1
# print(count)    

# ***************Method 2**************
char = input()
string = 'aeiouAEIOU'
count = 0
for c in char:
    if c in string:
        count+=1
print(count)