# 編號：CANDY-008

### 程式語言：Python

### 題目：傳入一字串，計算得分最高的字，英文字母 a 得 1 分、b 得 2 分、c 得 3 分，以此類推。所有傳入的字都是小寫。

```py
def highest_score_word(input):
    def word_score(word):
        return sum(ord(char) - ord("a") + 1 for char in word)

    words = input.split()
    highest_word = max(words, key=word_score)

    return highest_word

# 建立函數來計算每個字的得分
# 將輸入字串分割成單詞
# 使用 max() 找出得分最高的字

print(highest_score_word("lorem ipsum dolor sit amet"))
# 印出 ipsum
print(highest_score_word("heyn i need a rubygem up to build this"))
# 印出 rubygem
print(highest_score_word("in time machine there are some bugs"))
# 印出 there
```