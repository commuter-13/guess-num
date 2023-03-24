import time
import progressbar

# 讀取檔案
data = []
count = 0
bar = progressbar.ProgressBar(max_value=1000000)
with open("reviews.txt", "r")as f:
    for line in f:
        data.append(line)
        count += 1
        bar.update(count)
print("檔案讀取完了，總共有", len(data), "筆資料")

# 算每筆資料的平均長度
sum_len = 0
for x in data:
    sum_len += len(x)
print("平均長度為", sum_len/len(data))

# 篩選 資料的長度
new = []
for x in data:
    if len(x) < 100:
        new.append(x)
print("一共有", len(new), "筆留言的長度小於100")
print(new[0])

# good
good = []
for x in data:
    if "good" in x:
        good.append(x)
print("一共有", len(good), "筆留言提到good")
print(good[0])

# 文字計數
start_time = time.time()
wc = {}
for d in data:
    # split()預設值是空白鍵
    words = d.split()
    for word in words:
        if word in wc:
            wc[word] += 1
        else:
            # 新增新的key進wc字典
            wc[word] = 1

# 計算單字出現的次數
for word in wc:
    if wc[word] > 1000000:
        print(word, "出現的次數為", wc[word], "次")
end_time = time.time()

print("文字計數時間花了", end_time-start_time, "秒")
print("總共有幾個字:", len(wc))


while True:
    word = input("輸入想查詢的字:")
    if word == "q":
        break
    if word in wc:
        print(word, "出現的次數為", wc[word], "次")
    else:
        print("抱歉，查不到這個字")
print("結束")
