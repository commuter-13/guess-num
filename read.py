# 讀取檔案
data = []
count = 0
with open("reviews.txt", "r")as f:
    for line in f:
        data.append(line)
        count += 1
        if count % 10000 == 0:
            print(len(data))
print("檔案讀取完了，總共有", len(data), "筆資料")
print("第0筆的資料內容: ", data[0])

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

# 進階 快寫
good = [x for x in data if "good" in x]

bad = ["bad" in x for x in data]
print(bad)

bad = []
for x in data:
    bad.append("bad" in x)
print(bad)
