T = int(input())
win_lst = []

for tc in range(1, T+1):
    a, b, c = list(map(int, input().split()))

    if a == b == c:
        win = 10000+1000*a

    elif a == b != c:
        win = 1000+100*a
    elif a == c != b:
        win = 1000+100*a
    elif b == c != a:
        win = 1000+100*b
    
    else:
        win = 100*max(a,b,c)

    win_lst.append(win)

print(max(win_lst))