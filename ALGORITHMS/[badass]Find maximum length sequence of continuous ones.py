# n = int(input())
# arr = [int(x) for x in input().split()][:n]
# arr1 = []
# for i in range(len(arr)):
#     if arr[i]==0:
#         arr1.append(i)
# print(*arr1)


# n = int(input())
# arr = [int(x) for x in input().split()][:n]
# arr1 = []
# for i in range(len(arr)):
#     if arr[i]==0:
#         arr1.append(i)
# if len(arr1)==0:
#   print('Invalid input')
# else:
#   print(max(arr))
  
# n = int(input())
# arr = [int(x) for x in input().split()][:n]
# arr1 = []
# for i, x in enumerate(arr):
#     if x == 0:
#         arr1.append(i)
# if len(arr1)==0:
#     print('Invalid input')
# else:
#     print(max(arr1))

n = int(input())  # length of array
arr = [int(x) for x in input().split()][:n]

max_length = 0
max_index = -1

count = 0
prev_zero_index = -1
prev_prev_zero_index = -1

for i in range(n):
    if arr[i] == 1:
        count += 1
    else:
        if i - prev_prev_zero_index > max_length:
            max_length = i - prev_prev_zero_index
            max_index = prev_zero_index
        prev_prev_zero_index = prev_zero_index
        prev_zero_index = i
        count = i - prev_prev_zero_index

if n - prev_prev_zero_index > max_length:
    max_index = prev_zero_index

if max_length == 0 or max_index == -1:
    print('Invalid input')
else:
    print(max_index)