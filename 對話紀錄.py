# 讀取檔案
def read_file(fileName):
    lines = []
    with open(fileName, "r", encoding="utf-8-sig")as f:
        for line in f:
            lines.append(line.strip())
        return lines


# 轉換
def convert(lines):
    new = []
    # 預設值
    person = None
    for line in lines:
        if line == "Allen":
            person = "Allen"
            continue
        elif line == "Tom":
            person = "Tom"
            continue
        if person:
            new.append(person + ": " + line)
    return new


# 寫入檔案
def write_file(fileName, lines):
    with open(fileName, "w", encoding="utf-8") as f:
        for line in lines:
            f.write(line + "\n")


# 主要
def main():
    lines = read_file("input.txt")
    lines = convert(lines)
    write_file("output.txt", lines)


main()
