num = input()
arr = []
for c in num:
    x = int(c)**2
    arr.append(x)
arr.reverse()
print(*arr)
