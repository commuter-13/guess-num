products = []

while True:
    name = input("請輸入商品名稱：")
    if name == "q":
        break
    price = input("請輸入商品價格：")
    products.append([name, price])

print("完整清單:", products)

for item in products:
    print(item[0], "的價格是", item[1], "元")
