# 編號：CANDY-005

### 程式語言：Python

### 題目：完成函數的內容，把傳進去的數字的每個位數平方之後組合在一起

```py
def square_digits(num):
    num_list = list(str(num))
    numSquare = [str(int(num) ** 2) for num in num_list]
    return "".join(numSquare)

# 設定變數 num_list 使用 list 做切割, 由於數字沒辦法直接切割, 所以需要先轉成字串
# 設定變數 numSquare 使用推導式將 num 先轉成數字平方和, 由於 join() 需要使用字串所以再把 num 轉成字串
# 因為只有字串相加所以使用空字串, join() 會將轉成字串的數字做結合並回傳新的字串

print(square_digits(3212)) # 印出 9414
print(square_digits(2112)) # 印出 4114
print(square_digits(387)) # 印出 96449
```