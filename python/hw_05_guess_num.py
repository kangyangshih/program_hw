# DESC : 任務 5：終極密碼 (1~100)
# DESC : 作業內容請查看 https://hackmd.io/jaBX54-LS5mijHTFAQ7BAw
# DATE : 2026/2/7
import random

# 【需求說明】

# 電腦隨機產生一個 1~100 的數字。
num = random.randint(1, 100)

# 宣告兩個變數 min = 1 與 max = 100。
min = 1
max = 100

# 玩家猜測後，若沒中，要更新 min 或 max 並提示新範圍。
guess_count = 0
guess = input("請輸入數字:> ")

while int(guess) != num:
    if int(guess) > num:
        max = guess
        guess = input(f"請輸入 {min} 到 {max} 的數字:> ")
    elif int(guess) < num:
        min = guess
        guess = input(f"請輸入 {min} 到 {max} 的數字:> ")
    guess_count += 1

print(f"賓果！你總共猜了 {guess_count} 次")
