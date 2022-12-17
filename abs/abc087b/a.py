import itertools

a = int(input())
b = int(input())
c = int(input())
x = int(input())

result = 0

for v in itertools.product(list(range(a+1)), list(range(b+1))):
    remain = x - (v[0]*500 + v[1]*100)
    if remain >= 0:
        if remain % 50 == 0 and remain // 50 <= c:
            result += 1

print(result)
