#  編號：CANDY-016
#  程式語言：Python
#  題目：把原本 snake_case 的字轉換成 camelCase 格式
#  範例："hello_world" -> "helloWorld"
def toCamelCase(str):
    parts = str.split("_")

    camel_case = parts[0] + "".join(word.capitalize() for word in parts[1:])
    return camel_case


# 以底線分割字串成列表
# 將第一個部分保持小寫,其他部分首字母大寫後合併

print(toCamelCase("book"))  # book
print(toCamelCase("book_store"))  # bookStore
print(toCamelCase("get_good_score"))  # getGoodScore
