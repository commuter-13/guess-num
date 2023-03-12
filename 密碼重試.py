# 先設定好密碼 password="a123456"
# 最多輸入3次密碼
# 印出密碼錯誤，還有＿機會
# 登入成功

password = "a123456"
i = 3
while i > 0:
    i -= 1
    pwd = input("請輸入密碼:")
    if pwd == password:
        print("登入成功")
        break
    else:
        print("密碼錯誤")
        if i > 0:
            print("剩餘", i, "次機會\n")
        else:
            print(("登入失敗"))
