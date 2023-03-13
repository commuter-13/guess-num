import os

products = []
# 檢查檔案在不在
if os.path.isfile("products.csv"):
    print("開啟舊檔案")
    # 讀取檔案
    with open('products.csv', 'r', encoding="utf-8") as f:
        for line in f:
            if "商品,價格" in line:
                continue
            name, price = line.strip().split(",")
            products.append([name, price])
    print(products)
else:
    print("開啟新檔案")

# 使用者輸入
while True:
    name = input("請輸入商品名稱：")
    if name == "q":
        break
    price = input("請輸入商品價格：")
    price = int(price)
    products.append([name, price])
print("完整清單:", products)

# 印出所有購買紀錄
for p in products:
    print(p[0], "價格", p[1], "元")

# 印出總開銷
price = []
for p in products:
    price.append(p[1])

total = 0
for i in price:
    total += int(i)
print("總共消費:", total, "元")

# 寫入檔案
with open('products.csv', 'w', encoding="utf-8") as f:
    f.write("商品,價格\n")
    for p in products:
        f.write(p[0]+','+str(p[1])+'\n')
