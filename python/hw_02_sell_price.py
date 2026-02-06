# DESC : 任務 2：超市收銀系統 (折扣計算)
# DESC : 作業內容請查看 https://hackmd.io/jaBX54-LS5mijHTFAQ7BAw
# DATE : 2026/2/6

level_map = {
    "A": 0.8,
    "B": 0.85,
    "C": 0.9,
    "Non": 1,
}

bonus_map = {
    5000: 300,
    2000: 100,
}

# 取得資訊
price = float(input("請輸入商品原價:> "))
if price < 0:
    print("請輸入正確的價格")
    exit(1)
level = input("請輸入會員等級 (A/B/C/Non):> ")
if level not in level_map:
    print("請輸入正確的等級")
    exit(1)

# 計算折扣
discount = level_map[level]
total = price * discount
print(f"您的折扣為 {discount:.1f}, 總價為 {total:.0f}")

# 計算優惠
for bonus_price, bonus in bonus_map.items():
    if total >= bonus_price:
        total -= bonus
        print(f"獲得優惠 {bonus}, 總價為 {total:.0f}")
        break

print(f"總價為 {total:.0f}")
