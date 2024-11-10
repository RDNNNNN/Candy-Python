#  編號：CANDY-009
#  程式語言：Python
#  題目：移除網址中的錨點（Anchor）


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
