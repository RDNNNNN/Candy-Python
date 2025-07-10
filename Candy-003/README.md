# 編號：CANDY-003

### 程式語言：Python

### 題目：完成函數的內容，把陣列裡的 0 都移到最後面

```py
list = [False, 1, 0, -1, 2, 0, 1, 3, "a"]


def move_zeros_to_end(arr):
    list_not_zero = [i for i in arr if str(i) != "0"]
    list_zero = [i for i in arr if str(i) == "0"]
    return list_not_zero + list_zero

# 設定一個 list_not_zero 並使用推導式判斷不為 0 的值
# 設定一個 list_zero 並使用推導式判斷為 0 的值
# 利用串列相加後合併的特性並回傳串列

result = move_zeros_to_end(list)
print(result)
# 印出 [false, 1, -1, 2, 1, 3, "a", 0, 0]
```