# 編號：CANDY-025

### 程式語言：Python

### 題目：

一般我們常見的四捨五入計算方式在統計上容易造成計算偏差，於是有人推出了「銀行家捨入法」用來稍微平衡計算偏差，
計算方式是「四捨六入五成雙」，當捨入計算位數剛好是 5 的時候，會算出離這個數字比較近的偶數。

```py
def bankers_rounding(num, digits=0):

    factor = 10**digits

    rounded = round(num * factor) / factor

    if (num * factor) % 1 == 0.5:

        if int(rounded * factor) % 2 != 0:
            return (rounded - 0.1) if digits else int(rounded)

    return rounded

# 設定捨入的精度
# 四捨五入至指定的小數位
# 檢查是否有特殊的銀行家捨入情況
# 如果四捨五入後是 0.5 且為奇數，則向下捨入為偶數

print(bankers_rounding(0.4))  # 0
print(bankers_rounding(0.6))  # 1
print(bankers_rounding(0.5))  # 0
print(bankers_rounding(1.5))  # 2
print(bankers_rounding(1.24, 1))  # 1.2
print(bankers_rounding(1.26, 1))  # 1.3
print(bankers_rounding(1.25, 1))  # 1.2
```