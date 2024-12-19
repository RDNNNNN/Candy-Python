#  編號：CANDY-017
#  程式語言：Python
#  題目：計算數字的 2 進位裡有幾個 1
#  範例：5 -> 101 -> 2 個 1
def countBits(num):

    return bin(num).count("1")


# 將數字轉換為二進位字串，並計算 '1' 的數量

print(countBits(1234))  # 5
print(countBits(1450))  # 6
print(countBits(9527))  # 8
