#  編號：CANDY-013
#  程式語言：Python
#  題目：根據台灣財政部所提供的公司統編驗證規則，計算統一編號是否正確
#  https://www.fia.gov.tw/singlehtml/3?cntId=c4d9cff38c8642ef8872774ee9987283
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

print(is_valid_vat_number("10458575"))  #  true
print(is_valid_vat_number("88117125"))  # true
print(is_valid_vat_number("53212539"))  # true
print(is_valid_vat_number("88117126"))  # false
