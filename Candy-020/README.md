# 編號：CANDY-020

### 程式語言：Python

### 題目：檢查字串的 x 跟 o 的數量是不是一樣多，不分大小寫

```py
def xxoo(str):

    amount = str.lower()
    count_x = amount.count("x")
    count_o = amount.count("o")
    return count_x == count_o

# 將字串轉為小寫，然後計算 'x' 和 'o' 的次數

print(xxoo("ooxx"))  # true
print(xxoo("xxoo"))  # true
print(xxoo("xxooo"))  # false
print(xxoo("xoox"))  # true
print(xxoo("ooAA"))  # false
print(xxoo("xoXoA"))  # true
```