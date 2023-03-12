# 測驗 點餐系統

print("歡迎使用拉麵點餐機\n")
print("(1)鹽味拉麵 $220")
print("(2)醬油拉麵 $240")
print("(3)豚骨拉麵 $280\n")

soup = input("請選擇拉麵口味(輸入: 1 or 2 or 3)")

# .upper() 字母變大寫 | .lower() 字母變小寫
big = input("是否加大，豚骨口味+$50 其他口味+$30(輸入:Y or N)").upper()
egg = input("是否加糖心蛋+$30(輸入Y or N)").upper()
pork = input("是否加叉燒+$60(輸入Y or N)").upper()

bill = 0

# 選擇拉麵口味
if soup == "1":
    bill += 220
elif soup == "2":
    bill += 240
else:
    bill += 280

# 加大
if big == "Y":
    if soup == "3":
        bill += 50
    else:
        bill += 30

# 溏心蛋
if egg == "Y":
    bill += 30

# 叉燒
if pork == "Y":
    bill += 60

# 加好加滿 折扣$20
if big == "Y" and big == "Y" and egg == "Y" and pork == "Y":
    bill -= 20
    print(f"\n\n加好加滿,折扣$20, 總金額${bill}, 感謝您的光臨")
else:
    print(f"\n\n總金額${bill}, 感謝您的光臨")
