T = int(input())

for i in range(T):
    ox = list(map(str, input()))
    score = 0
    count = 1
    for i in ox:
        if i == 'O':
            score += count
            count += 1
        else:
            count = 1
    print(score)

#####################################

T = int(input())

for i in range(T):
    ox = list(map(str, input()))
    score = 0
    count = 1   
    for i in ox:
        if i == 'O':
            score += count
            count += 1
        else:
            count = 0
            score += count
    print(score)