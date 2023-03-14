# 讀取檔案
def read_file(fileName):
    lines = []
    with open(fileName, "r", encoding="utf-8-sig")as f:
        for line in f:
            lines.append(line.strip())
    return lines


# 計算 字 貼圖 圖片
def convert(lines):
    allen_word = 0
    allen_image = 0
    allen_sticker = 0

    viki_word = 0
    viki_image = 0
    viki_sticker = 0

    for line in lines:
        s = line.split(" ")
        time = s[0]
        name = s[1]
        if name == "Allen":
            if s[2] == "貼圖":
                allen_sticker += 1
            elif s[2] == "圖片":
                allen_image += 1
            else:
                for m in s[2:]:
                    allen_word += len(m)
        elif name == "Viki":
            if s[2] == "貼圖":
                viki_sticker += 1
            elif s[2] == "圖片":
                viki_image += 1
            else:
                for m in s[2:]:
                    viki_word += len(m)
    print("Allen傳了", allen_word, "字,", allen_sticker, "貼圖,", allen_image, "圖片")
    print("Viki傳了", viki_word, "字,", viki_sticker, "貼圖,", viki_image, "圖片")


# 主要
def main():
    lines = read_file("LINE-Viki.txt")
    lines = convert(lines)


main()
