n = int(input())
a = list(map(int, input().split()))

print(min([format(num, 'b')[::-1].find('1') for num in a]))
