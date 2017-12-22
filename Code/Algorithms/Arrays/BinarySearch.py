import random

# Nonpythonic


def find(a: list, start: int, end: int, n: int):

    if end - start == 1:
        return a[start] == n

    newedge = int((start + end) / 2)
    if n < a[newedge]:
        return find(a, start, newedge, n)
    else:
        return find(a, newedge, end, n)

# Pythonic without in


def pyfind(a: list, n: int):

    if len(a) == 1:
        return a[0] == n

    edge = int(len(a) / 2)
    if n < a[edge]:
        return pyfind(a[:edge], n)
    else:
        return pyfind(a[edge:], n)


u = sorted(set([int(random.random() * 1000) for x in range(200)]))
print(u)
for x in u:
    print(find(u, 0, len(u), x), pyfind(u, x), x in u)
