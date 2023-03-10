# 猜數字 提示：比大小

import random
start = int(input("數字範圍最小值："))
end = int(input("數字範圍最大值："))

ans = random.randint(start, end)
count = 0

while True:
    num = int(input("猜數字："))
    count += 1
    if num == ans:
        print("答對了")
        print("猜", count, "次")
        break
    elif num > ans:
        print("猜小一點")
    elif num < ans:
        print("猜大一點")
    print("猜", count, "次")
