#Приклад №1

class Stack:
    def __init__(self):
        self.items = []
        self._pop_counter = 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            return None
        self._pop_counter += 1
        return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0

    def get_counter(self):
        return self._pop_counter


stack = Stack()

stack.push(1)
stack.push(2)
stack.push(3)

print(stack.pop())  # 3
print(stack.pop())  # 2

stack.push(4)
stack.push(5)

print(stack.pop())  # 5

print(stack.get_counter())  # 3 (кількість операцій pop)

#Приклад №2

class QueueError(Exception):
    pass

class Queue:
    def __init__(self):
        self.items = []

    def put(self, element):
        self.items.insert(0, element)

    def get(self):
        if self.is_empty():
            raise QueueError("Queue error")
        return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0


queue = Queue()

queue.put(1)
queue.put("dog")

print(queue.get())  # 1
print(queue.get())  # dog

print(queue.is_empty())  # True

try:
    print(queue.get())
except QueueError as e:
    print("Queue error")

#Завдання 1

class QueueError(Exception):
    pass


class Queue:
    def __init__(self):
        self.items = []

    def put(self, element):
        self.items.insert(0, element)

    def get(self):
        if self.is_empty():
            raise QueueError("Queue error")
        return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0


class SuperQueue(Queue):
    def isempty(self):
        return self.is_empty()


que = SuperQueue()
que.put(1)
que.put("dog")
que.put(False)

for i in range(4):
    if not que.isempty():
        print(que.get())
    else:
        print("Queue empty")