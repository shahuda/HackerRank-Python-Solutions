from itertools import product

k, m = map(int, input().split())

lists = []
for _ in range(k):
    data = list(map(int, input().split()))
    lists.append(data[1:])

max_value = 0
for combo in product(*lists):
    value = sum(x**2 for x in combo) % m
    if value > max_value:
        max_value = value

print(max_value)

