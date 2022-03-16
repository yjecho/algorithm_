while True:
    n = int(input())
    if n == -1:
        break
    perfect_num = []
    for i in range(1, n):
        if n % i == 0:
            perfect_num.append(i)

    if sum(perfect_num) == n:
        print(n, " = ", " + ".joint(str(i) for i in perfect_num), sep = "")
    else:
        print(n, "is NOT perfect.")