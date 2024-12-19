# 編號：CANDY-018
#  程式語言：Python
#  題目：實作一個可以印出隨機整數的函數
import random


def random_number(min, max):

    if max is None:
        max = min
        min = 0

        # 隨機生成範圍 [min, max-1] 的整數
    return random.randint(min, max - 1)


# 只有一個參數時
# 將 min 作為上限
# 設定下限為 0
# 隨機生成範圍 [0, min-1] 的整數

print(random_number(50))  # 隨機印出 0 ~ 49 之間的任何一個數字
print(random_number(5, 30))  # 隨機印出 5 ~ 29 之間的任何一個數字
