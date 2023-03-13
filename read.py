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

# 算每筆資料的平均長度

sum_len = 0
for x in data:
    sum_len += len(x)

print("平均長度為", sum_len/len(data))
