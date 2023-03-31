# 密碼管理器
import json


# 讀取原有的檔案
def get_password_dic():
    with open("password.json", "r") as f:
        password_str = f.read()
        # 如果檔案是空的，回傳一個空字典
        if password_str == "":
            return {}
        else:
            # json 的 loads()函式 : 字串 轉換成 字典
            return json.loads(password_str)


# 檢查帳號名稱是否重複
def check_name(name):
    password_dic = get_password_dic()
    # keys() 取得字典裡所有的key
    if name in password_dic.keys():
        # 有重複的帳號名稱
        return False
    else:
        # 沒有重複的帳號名稱
        return True


# 新增帳號，寫入檔案
def add_password(name, account, password):
    # 檢查是否有重複的帳號名稱
    if check_name(name):
        # 先取得原有檔案中的資料
        password_dic = get_password_dic()
        # 新增
        password_dic[name] = {
            "account": account,
            "password": password
        }
        with open("password.json", "w") as f:
            # json 的 dumps()函式 : 字典 轉換成 字串
            f.write(json.dumps(password_dic))
        return True
    else:
        return False


print("\n密碼管理器")
while True:
    mode = input("\n請問要使用什麼功能? (請輸入字母)\n( a.查詢 | b.新增 | c.離開 )\n")
    if mode == "c":
        print("結束。")
        break
    elif mode == "b":
        name = input("請輸入帳號名稱:")
        account = input("請輸入帳號:")
        password = input("請輸入密碼:")
        if add_password(name, account, password):
            print("新增成功。")
        else:
            print("已有此帳號。")
    elif mode == "a":
        name = input("請輸入帳號名稱:")
        if check_name(name):
            print("無此帳號名稱。")
        else:
            password_dic = get_password_dic()
            account = password_dic[name]["account"]
            password = password_dic[name]["password"]
            print(f"帳號:{account}, 密碼{password}。")
