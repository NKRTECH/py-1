char = input()
hash = ''
alpha = ''
for c in char:
    if c=='#':
        hash+=c
for c in char:
    if c!='#':
        alpha+=c
print(hash+alpha)