# 編號：CANDY-022
# 程式語言：JavaScript
# 題目：實作 Queue 資料結構


class Queue:
    def __init__(self):

        self._elements = []

    @property
    def length(self):

        return len(self._elements)

    def enqueue(self, item=None):

        if item is not None:
            self._elements.append(item)

    def dequeue(self):

        if self._elements:
            return self._elements.pop(0)
        return None


# 使用列表來儲存隊列的元素
# 隊列的大小是列表長度
# 如果 item 不為 None, 則加入隊列
# 如果隊列不為空，取出第一個元素, 否則回傳 None

queue = Queue()
queue.enqueue(123)
queue.enqueue(456)
queue.enqueue()
print(queue.length)  # 印出 2

item = queue.dequeue()  # 取出元素
print(item)  # 印出 123

queue.dequeue()  # 繼續取出元素
print(queue.length)  # 印出 0
