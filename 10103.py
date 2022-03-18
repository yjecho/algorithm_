T = int(input())

cy = 100
sd = 100

for i in range(T):
    a,b = map(int, input().split())

    if a > b:
        sd += -a
    elif a < b:
        cy += -b
    else:
        sd += 0
        cy += 0

print(cy)
print(sd)