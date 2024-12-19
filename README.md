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

# 編號：CANDY-008

### 程式語言：Python

### 題目：

```py
傳入一字串，計算得分最高的字
英文字母 a 得 1 分、b 得 2 分、c 得 3 分，以此類推。
所有傳入的字都是小寫。
```

```py
def highest_score_word(input):
    def word_score(word):
        return sum(ord(char) - ord("a") + 1 for char in word)

    words = input.split()
    highest_word = max(words, key=word_score)

    return highest_word
# 建立函數來計算每個字的得分
# 將輸入字串分割成單詞
# 使用 max()找出得分最高的字

print(highest_score_word("lorem ipsum dolor sit amet"))
# 印出 ipsum
print(highest_score_word("heyn i need a rubygem up to build this"))
# 印出 rubygem
print(highest_score_word("in time machine there are some bugs"))
# 印出 there
```

# 編號：CANDY-009

### 程式語言：Python

### 題目：移除網址中的錨點（Anchor）

```py
def remove_anchor(url):
    url_split = url.split("#")
    return url_split[0]
# 設定變數url_split使用split()以'#'作為切割點
# 使用索引值並回傳前半段

print(remove_anchor("5xcampus.com"))  # 印出 5xcampus.com
print(remove_anchor("5xcampus.com/#about"))  # 印出 5xcampus.com/
print(
    remove_anchor("5xcampus.com/courses/?page=1#about")
)  # 印出 t5xcampus.com/courses/?page=1
```

# 編號：CANDY-010

### 程式語言：Python

### 題目：把數字以 10 進位展開式呈現，數字均為大於 0 的正整數

`範例：9527 變成 "1000 x 9 + 100 x 5 + 10 x 2 + 7"`

```py
def expanded_form(num):

    num_str = str(num)
    length = len(num_str)

    terms = [
        f"{10 ** (length - i - 1)} x {digit}"
        for i, digit in enumerate(num_str)
        if digit != "0"
    ]

    return " + ".join(terms)
# 使用 str() 將數字轉換為字串以便逐位處理
# 依序處理每一位數，忽略為 0 的位數
# 使用 ' + ' 連接各項非零的部分

print(expanded_form(8))  # 印出 8
print(expanded_form(25))  # 印出 10 x 2 + 5
print(expanded_form(148))  # 印出 100 x 1 + 10 x 4 + 8
print(expanded_form(1450))  # 印出 1000 x 1 + 100 x 4 + 10 x 5
print(expanded_form(60308))  # 印出 10000 x 6 + 100 x 3 + 8
```

# 編號：CANDY-011

### 程式語言：Python

### 題目：找出一個數字陣列裡，出現奇數次數的數字

```py
範例：[1, 1, 0]，`0` 只有出現 1 次
     [5, 5, 8, 8, 8, 4, 4]，`8` 出現了 3  次
```

```py
def find_odd_elm(numbers):

    result = 0
    for number in numbers:
        result ^= number
    return result
# 使用 XOR 運算符找出出現奇數次的數字

print(find_odd_elm([1, 1, 2]))  # 印出 2
print(find_odd_elm([5, 4, 2, 1, 5, 4, 2, 10, 10]))  # 印出 1
print(find_odd_elm([0, 1, 0, 1, 0]))  # 印出 0
print(find_odd_elm([1, 1, 2, -2, 5, 2, -1, -2, 5]))  # 印出 -1
print(find_odd_elm([20, 2, 2, 3, 3, 5, 5, 4, 20, 4, 5]))  # 印出 5
```

# 編號：CANDY-012

### 程式語言：Python

### 題目：把數字加總，最終濃縮成個位數

```py
範例：9527 => 9 + 5 + 2 + 7 => 23 => 2 + 3 => 5
     1450 => 1 + 4 + 5 + 0 => 10 => 1 + 0 => 1
```

```py
def number_reducer(num):

    while num >= 10:
        num = sum(int(digit) for digit in str(num))
    return num
# 寫一個 while 迴圈重複相加直到只剩下一位數

print(number_reducer(9527))  #  印出 5
print(number_reducer(1450))  #  印出 1
print(number_reducer(5566108))  #  印出 4
print(number_reducer(1234567890))  # / 印出 9
```

# 編號：CANDY-013

### 程式語言：Python

### 題目：根據台灣財政部所提供的公司統編驗證規則，計算統一編號是否正確

[規則網址](https://www.fia.gov.tw/singlehtml/3?cntId=c4d9cff38c8642ef8872774ee9987283)

```py
def is_valid_vat_number(vat):

    if len(vat) != 8 or not vat.isdigit():
        return False

    weights = [1, 2, 1, 2, 1, 2, 4, 1]

    total_sum = 0
    for i in range(8):
        product = int(vat[i]) * weights[i]
        total_sum += product // 10 + product % 10

    if vat[6] == "7":
        alternative_sum = total_sum - 1
        return total_sum % 5 == 0 or alternative_sum % 5 == 0
    else:
        return total_sum % 5 == 0
# 檢查是否為八位數字
# 定義權重
# 計算每位數字乘以權重後的結果
# 處理第七位數為 7 的特殊情況

print(is_valid_vat_number("10458575")) # true
print(is_valid_vat_number("88117125")) # true
print(is_valid_vat_number("53212539")) # true
print(is_valid_vat_number("88117126")) # false
```

# 編號：CANDY-014

### 程式語言：Python

### 題目：把鄰近的重複值去除，但仍照原本的順序排序

```py
  範例："AAABBBDDDAABBBCC" -> ['A', 'B', 'D', 'A', 'B', 'C']
```

```py
def unique_order(sequence):
    result = []
    prev = None

    for item in sequence:
        if item != prev:
            result.append(item)
            prev = item

    return result
# 使用 prev 變數來記錄上一個處理的值
# 如果當前元素與前一個不同，则將其加入結果陣列中
# 更新 prev 為當前元素

print(unique_order("AABCC"))  # [ 'A', 'B', 'C']
print(unique_order("AAABBBCCBCC"))  # [ 'A', 'B', 'C', 'B', 'C']
print(unique_order([1, 2, 1, 2, 1]))  # [ 1, 2, 1, 2, 1 ]
print(unique_order([1, 1, 1, 2, 2, 2, 1]))  # [1, 2, 1]
```

# 編號：CANDY-015

### 程式語言：Python

### 題目：把原本的字串拆解成 2 個字元一組，若不足 2 個字則補上底線

```py
範例：
   "abcdef" -> ['ab', 'cd', 'ef']
   "abcdefg" -> ['ab', 'cd', 'ef', 'g_']
```

```py
def split_string(str):
    result = []
    length = len(str)

    for i in range(0, length, 2):
        if i + 1 < length:
            result.append(str[i : i + 2])
        else:
            result.append(str[i] + "_")

    return result


# result 用於儲存分組後的結果
# length 用於計算字串的長度
# 每次取兩個字元
# 確認還有兩個字元
# 將兩個字元加入結果
# 最後一個字元不足兩個，補上底線

print(split_string("abcdef"))  # ["ab", "cd", "ef"]
print(split_string("abcdefg"))  # ["ab", "cd", "ef", "g_"]
print(split_string(""))  # []
```

# 編號：CANDY-016

### 程式語言：Python

### 題目：把原本 snake_case 的字轉換成 camelCase 格式

```py
  範例："hello_world" -> "helloWorld"
```

```py
def toCamelCase(str):
    parts = str.split("_")

    camel_case = parts[0] + "".join(word.capitalize() for word in parts[1:])
    return camel_case


# 以底線分割字串成列表
# 將第一個部分保持小寫, 其他部分首字母大寫後合併

print(toCamelCase("book"))  # book
print(toCamelCase("book_store"))  # bookStore
print(toCamelCase("get_good_score"))  # getGoodScore
```
