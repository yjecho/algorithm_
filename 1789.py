s = int(input())
i = 0
sum = 0

while True:
    i += 1
    sum1 = (i*(i+1))/2
    sum2 = ((i+1)*(i+2))/2

    if sum1 <= s and sum2>s:
        break

print(i)