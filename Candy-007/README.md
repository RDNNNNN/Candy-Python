# 編號：CANDY-007

### 程式語言：Python

### 題目：在某個數字陣列裡，可能藏有某個不合群的奇數或偶數，試著找出它！

```py
def find_some_different(numbers):
    odds = [num for num in numbers if num % 2 == 0]
    evens = [num for num in numbers if num % 2 != 0]
    return odds[0] if len(odds) == 1 else evens[0]

# 設定變數 odds 並使用推導式判斷偶數
# 設定變數 enevs 並使用推導式判斷奇數
# 使用 pop() 抓出串列的值並判斷長度是 1 後回傳

print(find_some_different([2, 4, 0, 100, 4, 11, 2602, 36]))  # 印出 11
print(find_some_different([160, 3, 1719, 19, 11, 13, -21]))  # 印出 160
```