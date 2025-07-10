# 編號：CANDY-014

### 程式語言：Python

### 題目：把鄰近的重複值去除，但仍照原本的順序排序

```py
範例：

"AAABBBDDDAABBBCC" -> ['A', 'B', 'D', 'A', 'B', 'C']
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