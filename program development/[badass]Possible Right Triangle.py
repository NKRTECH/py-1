peri = int(input())
# count=0
# # arr1 =[]
# for i in range(peri):
#     for j in range(peri):
#         for k in range(peri):
#             if i**2+j**2==k**2 and i+j+k==peri:
#                 if i+j>k and j+k>i and i+k>j and abs(i-j)<k and abs(j-k)<i and abs(k-i)<j:
#                     count+=1
#                     break
#                     # arr1.append([i,j,k])
# # print(arr1)
# if count>0:
#     print('Yes')
# else:
#     print('No')
    
if any(i**2+j**2==k**2 and i+j+k==peri and i+j>k and j+k>i and i+k>j and abs(i-j)<k and abs(j-k)<i and abs(k-i)<j for i in range(peri) for j in range(peri) for k in range(peri)):
    print('Yes')
else:
    print('No')
    
    
p=int(input())
flag=False 
for a in range(1,p//2):
    for b in range(1,p//3):
        c=p-a-b
        if a+b>c and a+c>b and b+c>a:
            if a**2+b**2==c**2:
                flag=True
                break   
if flag:
    print("Yes")
else:
    print("No")