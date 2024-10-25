# 編號：CANDY-001

### 程式語言：Python

### 題目：找出陣列裡最小的兩個值的總和

### 例如：

`[15, 28, 4, 2, 43] 印出 6`

`[23, 71, 33, 82, 1] 印出 24`

```py
def sum_of_smallest_values(arr):
    sorted_arr = sorted(arr)
    return sorted_arr[0] + sorted_arr[1]


# 使用 sorted() 方法排序, sorted() 預設會是由小到大排序
# 使用索引值取得最小的兩個值並相加
list1 = [19, 5, 42, 2, 77]
list2 = [23, 15, 59, 4, 17]

print(sum_of_smallest_values(list1))  # 印出 7
print(sum_of_smallest_values(list2))  # 印出 19
```

# 編號：CANDY-002

### 程式語言：Python

### 題目：請寫一小段程式，印出連續陣列裡缺少的字元

```py
chars1 = ["a", "b", "c", "d", "f", "g"]
chars2 = ["O", "Q", "R", "S"]


def missing_char(chars):
    char_loop = set(ord(char) for char in chars)
    char_range = set(range(ord(chars[0]), ord(chars[-1]) + 1))
    return chr((char_range - char_loop).pop())


# 在 set() 中寫一個迴圈並使用 ord() 將字串轉成數字
# 使用 range() 設定迴圈範圍的第一個值跟最後一個值,可以抓出連續的值, + 1 是確保能包含最後一位
# 利用 set() 能移除重複值的特性,將迴圈的內容跟 range() 的內容相減,就能找出缺少的數字
# 使用 chr() 將數字轉成字串,因為 set() 本身有 {},使用 pop() 顯示移除的值並回傳


print(missing_char(chars1))  # 印出 e
print(missing_char(chars2))  # 印出 P

#  提示：
#  可使用字串的 charCodeAt 方法...
```
