n = int(input())
arr = [int(x) for x in input().split()][:n]
m = int(input())
if any(abs(arr[i] - arr[j]) == m for i in range(len(arr)) for j in range(i+1, len(arr))): # define i before j in the for loop because i is used in the for loop of j 
    #otherwise it will give error "i is not defined"
    print('1')
else:
    print('0')

def kdiff(arr,m):
    if any(abs(arr[i] - arr[j]) == m for i in range(len(arr)) for j in range(i+1, len(arr))): 
        return('1')
    else:
        return('0')
n = int(input())
arr = [int(x) for x in input().split()][:n]
m = int(input())
print(kdiff(arr,m))
