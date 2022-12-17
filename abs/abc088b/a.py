n = int(input())
a = list(map(int, input().split()))

a_sum = 0
b_sum = 0

a.sort(reverse=True)

for i in range(n):
    if i % 2 :
        b_sum += a[i]
    else:
        a_sum += a[i]

print(a_sum-b_sum) 

