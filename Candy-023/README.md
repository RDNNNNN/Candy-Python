# 編號：CANDY-023

### 程式語言：Python

### 題目：算出 N 個數字的最大公因數

```py
from math import gcd
from functools import reduce


def calc_gcd(*numbers):

    return reduce(gcd, numbers)

# 使用 reduce 將列表中的數字逐步計算 GCD

print(calc_gcd(10))  # 10
print(calc_gcd(103, 27))  # 1
print(calc_gcd(21, 15, 18))  # 3
print(calc_gcd(104, 96, 36, 88))  # 4
```