# 密碼產生器

import random

letters_upper = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K",
                 "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
letters_lower = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k",
                 "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbols = ["!", "@", "#", "$", "%", "^", "&", "*", "-", "+"]


print("密碼產生器")


b_input = int(input("請問需要幾個大寫字母 :"))
s_input = int(input("請問需要幾個小寫字母 :"))
num_input = int(input("請問需要幾個數字 :"))
sym_input = int(input("請問需要幾個符號 :"))

# letters_upper[random.randint(0,25)] 隨機取1個字母

password = ""

for i in range(0, b_input):
    password += letters_upper[random.randint(0, 25)]


for i in range(0, s_input):
    password += letters_lower[random.randint(0, 25)]

for i in range(0, num_input):
    password += numbers[random.randint(0, 9)]

for i in range(0, sym_input):
    password += symbols[random.randint(0, 9)]

print(f"密碼:{password}")


# 字串 轉換 列表
list_p = list(password)

# 列表 打亂
random.shuffle(list_p)

# 用for迴圈 將 列表 轉換成 字串
new_password = ""
for i in list_p:
    new_password += i

print(f"隨機密碼:{new_password}")
