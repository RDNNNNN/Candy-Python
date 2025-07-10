# 編號：CANDY-006

### 程式語言：Python

### 題目：找出在數字陣列裡跟其它元素不一樣的值

```py
def find_different(numbers):
    set_num = (num for num in set(numbers) if numbers.count(num) == 1)
    return next(set_num)

# 設定變數 set_num 使用推導式, 將串列轉成 set() 取出重複值
# 因為只有一個不重複值, 使用 count() 判斷出現的值是否為 1
# 使用 pop() 可以移除此元素並回傳

print(find_different([1, 1, 1, 1, 3, 1, 1, 1]))  # 印出 3
print(find_different([2, 2, 2, 4, 2, 2]))  # 印出 4
print(find_different([8, 3, 3, 3, 3, 3, 3, 3]))  # 印出 8
```