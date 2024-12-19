#  編號：CANDY-004
#  程式語言：Python
#  題目：完成函數的內容，把傳進去的秒數變成平常人類看的懂的時間格式


def human_readable_timer(seconds):
    hour = seconds // 3600
    min = (seconds % 3600) // 60
    sec = seconds % 60

    return f"{hour:02}:{min:02}:{sec:02}"


# 設定 hour 為小時, 3600 秒進位小時, 所以除以 3600
# 設定 min 為分鐘, 3600 秒進位小時所以取 3600 餘數,60 秒進位分鐘所以除以 60
# 設定 sec 為秒, 60 秒進位分鐘, 所以取 60 餘數
# 使用 f 字串設定兩位數並回傳


print(human_readable_timer(0))  # 印出 00:00:00
print(human_readable_timer(59))  # 印出 00:00:59
print(human_readable_timer(60))  # 印出 00:01:00
print(human_readable_timer(90))  # 印出 00:01:30
print(human_readable_timer(3599))  # 印出 00:59:59
print(human_readable_timer(3600))  # 印出 01:00:00
print(human_readable_timer(45296))  # 印出 12:34:56
print(human_readable_timer(86399))  # 印出 23:59:59
print(human_readable_timer(86400))  # 印出 24:00:00
print(human_readable_timer(359999))  # 印出 99:59:59
