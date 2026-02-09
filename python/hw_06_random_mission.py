# DESC : 任務 6：隨機清單分析器
# DESC : 作業內容請查看 https://hackmd.io/jaBX54-LS5mijHTFAQ7BAw
# DATE : 2026/2/9

# 系統自動產生一個包含 20 個隨機整數（範圍 1~100）的 List
import random

random_list = [random.randint(1, 100) for _ in range(20)]
print(random_list)

# 做排序後做印出
random_list.sort()
print(random_list)

# 找出清單中的最大值與最小值
max_num = max(random_list)
min_num = min(random_list)
print(f"最大值為 {max_num}, 最小值為 {min_num}")

# 計算所有數字的總和與平均值。
total = sum(random_list)
average = total / len(random_list)
print(f"總和為 {total}, 平均值為 {average}")

# 建立一個新的 List，只存放原清單中的偶數
even_list = [num for num in random_list if num % 2 == 0]
print(f"偶數清單為 {even_list}")
