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


# 使用sorted()方法排序,sorted()預設會是由小到大排序
# 使用索引值取得最小的兩個值並相加
list1 = [19, 5, 42, 2, 77]
list2 = [23, 15, 59, 4, 17]

print(sum_of_smallest_values(list1))  # 印出 7
print(sum_of_smallest_values(list2))  # 印出 19
```
