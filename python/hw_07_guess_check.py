# DESC : 任務 7：安全輸入檢查器
# DESC : 作業內容請查看 https://hackmd.io/jaBX54-LS5mijHTFAQ7BAw
# DATE : 2026/2/9


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


# 請使用者輸入一個字串
password = input("請輸入字串:> ")

# 檢查字串是否符合規則
check_res = check_guess_num(password)
if check_res == "":
    print("字串符合規則")
else:
    print(f"字串不符合規則 : {check_res}")
