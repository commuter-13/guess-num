# 自我介紹
print("自我介紹產生器")
name = input("請輸入名字：")
age = input("請輸入年紀：")
hobby = input("請輸入興趣：")

print("大家好，我是" + name + "，今年" + age + "歲，我的興趣是" + hobby + "，很高興認識大家！")

# f-string
name = "宅宅"
age = 27
height = 180.5
is_male = True
print(f"{name}今年{age}歲，身高{height}公分，是否為男生：{is_male}")

# 資料型態
# 字串 string
print("李晨瑋")

# 字串的第0順位
print("李晨瑋"[0])

name = "咒術回戰"
print(name[2])

print('李晨瑋"每天"打掃房間')
print("李晨瑋\"每天\"打掃房間")
print("換行\n咒術迴戰")

# 整數 int
print(27)

num = 10_000_000
print(num)

# 浮點數 float
print(23.5)

# 布林值 boolean
True
False

# 運算符號 數字用法
# ()
# **（次方） //（求整數）
# * / %(求餘數)
# + -

# 四捨五入
print(round(1.66666, 3))

# 轉換資料型態
num1 = int(input("請輸入第一個數字"))
num2 = int(input("請輸入第二個數字"))
print(num1 + num2)

# 測驗 第一位數 與 第二位數 相加
numbers = input("請輸入一個兩位數數字")
number1 = int(numbers[0])
number2 = int(numbers[1])
print(number1 + number2)

# 測驗 BMI計算機
height = float(input("請輸入身高（公分）\n"))
weight = float(input("請輸入體重（公斤）\n"))
height = height / 100
BMI = weight / height**2
BMI = round(BMI, 1)
print(f"你的BMI:{BMI}")
