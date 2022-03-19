from re import S


T = int(input())

for _ in range(T):
    school = {}
    N = int(input())

    for _ in range(N):
        a,b = map(str, input().split())
        school[a] = int(b)
    swap_school = dict(zip(school.values(), school.keys()))
    print(swap_school[max(swap_school)])