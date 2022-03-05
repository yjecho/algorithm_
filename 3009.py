x_nums = []
y_nums = []

for _ in range(3):
    x, y = map(int, input().split())
    x_nums.append(x)
    y_nums.append(y)

for i in range(3):
    if x_nums.count(x_nums[i]) == 1:
        x_answer = x_nums[i]
    if y_nums.count(y_nums[i]) == 1:
        y_answer = y_nums[i]

print(x_answer, y_answer)