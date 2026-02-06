# DESC : 任務 4：星號圖形繪製大挑戰
# DESC : 作業內容請查看 https://hackmd.io/jaBX54-LS5mijHTFAQ7BAw
# DATE : 2026/2/7

# 取得資訊
num = int(input("請輸入數字:> "))

# 畫左下直角三角形
print("\n~~~~~~~~")
for i in range(1, num + 1):
    for j in range(1, i + 1):
        print("*", end="")
    print()

# 畫左上直角三角形
print("\n~~~~~~~~")
for i in range(num, 0, -1):
    for j in range(1, i + 1):
        print("*", end="")
    print()

# 畫正方形
print("\n~~~~~~~~")
for i in range(1, num + 1):
    for j in range(1, num + 1):
        print("*", end="")
    print()

# 靠右直角三角
print("\n~~~~~~~~")
for i in range(1, num + 1):
    for j in range(1, num - i + 1):
        print(" ", end="")
    for k in range(1, i + 1):
        print("*", end="")
    print()

# 等腰三角形
print("\n~~~~~~~~")
#   *
#  ***
# *****
for i in range(1, num + 1):
    for j in range(1, num - i + 1):
        print(" ", end="")
    for k in range(1, i * 2):
        print("*", end="")
    print()
