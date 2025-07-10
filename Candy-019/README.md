# 編號：CANDY-019

### 程式語言：Python

### 題目：檢查是否為某個數字的平方數

```py
def is_square(num):
    import math

    if num < 0:
        return False
    sqrt_num = int(math.sqrt(num))
    return sqrt_num * sqrt_num == num


# 匯入 math 模組, 判斷 num < 0 時為 False
# 使用 math.sqrt() 得到數字的平方根, 並使用 int() 轉成整數
# 判斷平方根相乘是否等於原來的數字並回傳

print(is_square(0))  # True
print(is_square(4))  # True
print(is_square(5))  # False
print(is_square(100))  # True
print(is_square(-4))  # False
print(is_square(-1))  # False
```