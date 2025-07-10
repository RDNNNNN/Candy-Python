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