char = [x for x in input()]
char1 = ''
# char.sort()
# print(char)
for c in char:
    if c.isalpha():
        char1+=c
# for c in char:
#     if c!='#' and not c.isalpha():
#         char1+=c
# print(char1)   // input:ka##lviu$%m  output:kalvium$%
for c in char:
    if c=='#':
        char1+=c
print(char1)