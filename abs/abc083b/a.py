n, a, b = map(int, input().split())

def some_sums(num: int) -> int:
    dig = len(str(num))
    some_sum = 0
    while dig >= 0:
        some_sum += (num // (10**dig))
        num = num % (10**dig)
        dig -= 1
    return some_sum

ans = 0

for num in range(1, n+1):
    if a <= some_sums(num) <= b:
        ans += num

print(ans)

