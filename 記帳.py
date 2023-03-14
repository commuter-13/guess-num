# operating system
import os


# 讀取檔案
def read_file(fileName):
    products = []
    with open(fileName, 'r', encoding="utf-8") as f:
        for line in f:
            if "商品,價格" in line:
                continue
            name, price = line.strip().split(",")
            products.append([name, price])
    return products


# 輸入商品
def user_input(products):
    while True:
        name = input("請輸入商品名稱：")
        if name == "q":
            break
        price = input("請輸入商品價格：")
        price = int(price)
        products.append([name, price])
    print("完整清單:", products)
    return products


# 印出 所有購買紀錄
def print_products(products):
    for p in products:
        print(p[0], "價格", p[1], "元")


# 寫入檔案
def write_file(fileName, products):
    with open(fileName, 'w', encoding="utf-8") as f:
        f.write("商品,價格\n")
        for p in products:
            f.write(p[0]+','+str(p[1])+'\n')


# 主要執行
def main():
    fileName = "products.csv"
    if os.path.isfile(fileName):
        print("找到檔案，開啟舊檔案")
        products = read_file(fileName)
    else:
        products = []
        print("開啟新檔案")
    products = user_input(products)
    print_products(products)
    write_file("products.csv", products)


main()
