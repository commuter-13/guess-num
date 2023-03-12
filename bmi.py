heigh = int(input("請輸入身高(公分):"))
weight = int(input("請輸入體重(公斤):"))
BMI = weight / (heigh/100)**2

print("身高=", heigh, "公分")
print("體重=", weight, "公斤")

if BMI < 18.5:
    print("BMI=", round(BMI, 1), ",體重過輕")
elif BMI >= 18.8 and BMI < 24:
    print("BMI=", round(BMI, 1), ",正常範圍")
elif BMI >= 24 and BMI < 27:
    print("BMI=", round(BMI, 1), ",稍重")
elif BMI > 27 and BMI < 30:
    print("BMI=", round(BMI, 1), ",輕度肥胖")
elif BMI >= 30 and BMI < 35:
    print("BMI=", round(BMI, 1), ",中度肥胖")
else:
    print("BMI=", round(BMI, 1), ",重度肥胖")
