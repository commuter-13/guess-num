lines = []
with open('對話3.txt', 'r', encoding='utf-8-sig') as f:
    for line in f:
        lines.append(line.strip())

# 取出所有名字
for line in lines:
    s = line.split(' ')
    time = s[0][:5]
    name = s[0][5:]
    print(name)
