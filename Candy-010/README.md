# 編號：CANDY-010

### 程式語言：Python

### 題目：把數字以 10 進位展開式呈現，數字均為大於 0 的正整數

```py
範例：9527 變成 "1000 x 9 + 100 x 5 + 10 x 2 + 7"
```

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