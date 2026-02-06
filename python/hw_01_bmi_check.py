# DESC : 任務 1：BMI 健康檢測器
# DESC : 作業內容請查看 https://hackmd.io/jaBX54-LS5mijHTFAQ7BAw
# DATE : 2026/2/6

name = input("請輸入你的名字:> ")
height = float(input("請輸入你的身高(cm):> "))
weight = float(input("請輸入你的體重(kg):> "))

bmi = weight / (height / 100)**2
print(f"{name} 的 BMI 為 {bmi:.2f}")

if bmi < 18.5:
    state = "體重過輕"
elif bmi < 24:
    state = "體重正常"
elif bmi < 27:
    state = "體重過重"
else:
    state = "體重肥胖"

print(f"{name} 您好，您的 BMI 為 {bmi:.2f}，狀態為：{state}")
