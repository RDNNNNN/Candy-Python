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

# 編號：CANDY-004

### 程式語言：Python

### 題目：完成函數的內容，把傳進去的秒數變成平常人類看的懂的時間格式

```py
def human_readable_timer(seconds):
    hour = seconds // 3600
    min = (seconds % 3600) // 60
    sec = seconds % 60

    return f"{hour:02}:{min:02}:{sec:02}"

# 設定 hour 為小時, 3600 秒進位小時, 所以除以 3600
# 設定 min 為分鐘, 3600 秒進位小時所以取 3600 餘數, 60 秒進位分鐘所以除以 60
# 設定 sec 為秒, 60 秒進位分鐘, 所以取 60 餘數
# 使用 f 字串設定兩位數並回傳

print(human_readable_timer(0))  # 印出 00:00:00
print(human_readable_timer(59))  # 印出 00:00:59
print(human_readable_timer(60))  # 印出 00:01:00
print(human_readable_timer(90))  # 印出 00:01:30
print(human_readable_timer(3599))  # 印出 00:59:59
print(human_readable_timer(3600))  # 印出 01:00:00
print(human_readable_timer(45296))  # 印出 12:34:56
print(human_readable_timer(86399))  # 印出 23:59:59
print(human_readable_timer(86400))  # 印出 24:00:00
print(human_readable_timer(359999))  # 印出 99:59:59
```
