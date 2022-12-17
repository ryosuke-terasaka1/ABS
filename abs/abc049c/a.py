s = input()

t_set = {'dream', 'dreamer', 'erase', 'eraser'}

i = -1
length = len(s)

while abs(i) <= length:
    if s[i:] in t_set:
        s = s[:i]
        length = len(s)
        i = -1
    else:
        i -= 1

if s:
    print('NO')
else:
    print('YES')
