n = int(input())

is_ok = True
t_n, x_n, y_n = 0, 0, 0

for _ in range(n):
    t, x, y = map(int, input().split())
    t_n = abs(t - t_n)
    x_n = abs(x - x_n)
    y_n = abs(y - y_n)

    if not (t_n >= x_n+y_n and t_n%2==(x_n+y_n)%2):
        is_ok = False
        break

if is_ok:
    print('Yes')

else: print('No')  

