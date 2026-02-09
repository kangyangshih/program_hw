# DESC : 任務 8：1A2B 益智遊戲
# DESC : 作業內容請查看 https://hackmd.io/jaBX54-LS5mijHTFAQ7BAw
# DATE : 2026/2/9

import random
import os


# function
# input : str
# output : str
# "" : pass
# 規則:
# 1. 長度必須剛好是 4 位
# 2. 必須全部都是數字（不能有英文）
# 3. 數字不能重複
def check_guess_num(password):
    if len(password) != 4:
        return "長度必須剛好是 4 位"
    if not password.isnumeric():
        return "必須全部都是數字（不能有英文）"
    if len(set(password)) != 4:
        return "數字不能重複"
    return ""


# 初始化：電腦產生 4 個不重複的隨機數字 (0~9) 作為謎底
secret = ""
while True:
    secret = "".join(str(random.randint(0, 9)) for _ in range(4))
    check_res = check_guess_num(secret)
    if check_res == "":
        break
    print(f"secret : {secret} 謎底不符合規則({check_res})，請重新產生謎底")
    # os.system("pause")
# 開始遊戲
print(f"謎底為 {secret}")

counter = 0
while True:
    # 請使用者輸入一個字串
    guess = input("請輸入猜測字串:> ")
    counter += 1
    # 檢查字串是否符合規則
    check_res = check_guess_num(guess)
    if check_res != "":
        print(f"再猜, 字串不符合規則 : {check_res}")
        continue
    # 比對謎底與猜測字串
    a = 0
    b = 0
    for i in range(4):
        if guess[i] == secret[i]:
            a += 1
        elif guess[i] in secret:
            b += 1
    # 印出結果
    print(f"[{counter}] 猜測字串 {guess} : {a}A{b}B")
    if a == 4:
        print(f"賓果！你總共猜了 {counter} 次")
        break
