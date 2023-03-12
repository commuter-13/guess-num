# 綜合健康計算機   BMI | 基礎代謝率（BMR) | 總熱量消耗(TDEE)

def get_bmi(height, weight):
    height = height / 100
    bmi = weight / height**2
    bmi = round(bmi, 1)
    return bmi


def get_bmr(sex, height, weight, age):
    if sex == "男":
        bmr = 66 + 13.7*weight + 5*height - 6.8*age
    else:
        bmr = 655 + 9.6*weight + 1.8*height - 4.7*age
    bmr = round(bmr, 2)
    return bmr


def get_tdee(sex, height, weight, age, times):
    bmr = get_bmr(sex, height, weight, age)
    tdee = bmr*times
    tdee = round(tdee, 2)
    return tdee


print("\n歡迎使用綜合健康計算機")
while True:
    number = input(
        "\n(1)計算BMI (2)計算基礎代謝率(BMR) (3)計算總熱量消耗(TDEE) (4)結束\n請選擇要計算的項目:")
    if number == "1":
        height = float(input("\n請輸入身高(公分):"))
        weight = float(input("\n請輸入體重(公斤):"))
        bmi = get_bmi(height, weight)

        if bmi < 18.5:
            print("\nBMI=", round(bmi, 1), ",體重過輕")
        elif bmi >= 18.8 and bmi < 24:
            print("\nBMI=", round(bmi, 1), ",正常範圍")
        elif bmi >= 24 and bmi < 27:
            print("\nBMI=", round(bmi, 1), ",稍重")
        elif bmi > 27 and bmi < 30:
            print("\nBMI=", round(bmi, 1), ",輕度肥胖")
        elif bmi >= 30 and bmi < 35:
            print("\nBMI=", round(bmi, 1), ",中度肥胖")
        else:
            print("\nBMI=", round(bmi, 1), ",重度肥胖")
        continue

    elif number == "2":
        sex = input("\n請輸入性別 (男 or 女):")
        height = float(input("\n請輸入身高(公分):"))
        weight = float(input("\n請輸入體重(公斤):"))
        age = int(input("\n請輸入年齡:"))
        bmr = get_bmr(sex, height, weight, age)
        print(f"\n基礎代謝率(BMR) : {bmr}")
        continue

    elif number == "3":
        sex = input("\n請輸入性別 (男 or 女):")
        height = float(input("\n請輸入身高(公分):"))
        weight = float(input("\n請輸入體重(公斤):"))
        age = int(input("\n請輸入年齡:"))

        print("\n(1)久坐、幾乎沒運動 (2)低強度運動 (3)中強度運動 (4)高強度運動 (5)高強度運動")
        exer = input("\n請選擇運動量(輸入1~5):")

        times = 0
        if exer == "1":
            times = 1.2
        elif exer == "2":
            times = 1.375
        elif exer == "3":
            times = 1.55
        elif exer == "4":
            times = 1.725
        else:
            times = 1.9

        tdee = get_tdee(sex, height, weight, age, times)
        print(f"\n總消耗熱量(TDEE):{tdee}")
        continue

    elif number == "4":
        print("\nGOODBYE\n")
        break

    else:
        print("\n請重新輸入")
        continue
