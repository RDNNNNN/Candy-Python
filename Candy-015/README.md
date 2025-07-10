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