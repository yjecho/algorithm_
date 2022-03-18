T = int(input())

for i in range(T):
    y = 0
    k = 0

    for j in range(9):
        yon,kor = map(int, input().split())
        y += yon
        k += kor

    if y == k:
        print("Draw")
    elif y > k:
        print("Yonsei")
    else:
        print("Korea")