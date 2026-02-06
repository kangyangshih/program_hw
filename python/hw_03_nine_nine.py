# DESC : 任務 3：九九乘法表排版
# DESC : 作業內容請查看 https://hackmd.io/jaBX54-LS5mijHTFAQ7BAw
# DATE : 2026/2/7

for i in range(1, 10):
    for j in range(1, 10):
        print(f"{i} * {j} = {i * j:>2}", end="\t")
    print()
