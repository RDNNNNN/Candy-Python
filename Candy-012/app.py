# 編號：CANDY-012
# 程式語言：Python
# 題目：把數字加總，最終濃縮成個位數
# 範例：9527 => 9 + 5 + 2 + 7 => 23 => 2 + 3 => 5
#      1450 => 1 + 4 + 5 + 0 => 10 => 1 + 0 => 1


def number_reducer(num):

    while num >= 10:
        num = sum(int(digit) for digit in str(num))
    return num


# 寫一個 while 迴圈重複相加直到只剩下一位數

print(number_reducer(9527))  #  印出 5
print(number_reducer(1450))  #  印出 1
print(number_reducer(5566108))  #  印出 4
print(number_reducer(1234567890))  # / 印出 9
