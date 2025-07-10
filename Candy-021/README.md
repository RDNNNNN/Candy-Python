# 編號：CANDY-021

### 程式語言：Python

### 題目：實作 Stack 資料結構

```py
class Stack:
    def __init__(self):

        self._elements = []

    @property
    def size(self):

        return len(self._elements)

    def push(self, item=None):

        if item is not None:
            self._elements.append(item)

    def pop(self):

        if self._elements:
            return self._elements.pop()
        return None

# 使用列表來儲存堆疊的元素
# 堆疊的大小是列表長度
# 如果 item 不為 None，則加入堆疊
# 如果堆疊不為空，取出最後一個元素，否則回傳 None

stack = Stack()
stack.push(123)
stack.push(456)
stack.push()
print(stack.size)  # 印出 2

item = stack.pop()  # 取出元素
print(item)  # 印出 456

stack.pop()  # 繼續取出元素
print(stack.size)  # 印出 0
```