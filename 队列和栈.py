#栈的python代码实现
#先进后出
class Stack(object):
    def __init__(self):
        self.stack = []

    def pop(self):
        if self.is_empty():
            return None
        else:
            return self.stack.pop()

    def push(self,val):
        return self.stack.append(val)

    def is_empty(self):
        return self.size() == 0

    def size(self):
        return len(self.stack)

    def peak(self):
        if self.is_empty():
            return None
        else:
            return self.stack[-1]

s = Stack()
s.push(1)
s.peak()
s.is_empty()
s.pop()
#队列的python代码实现
#先进先出
class Queue(object):
    def __init__(self):
        self.queue = []

    def enqueue(self,val):
        self.queue.insert(0,val)

    def dequeue(self):
        if self.is_empty():
            return None
        else:
            return self.queue.pop()

    def is_empty(self):
        return self.size == 0

    def size(self):
        return len(self.queue)

q = Queue()
q.enqueue(1)
q.is_empty()
q.dequeue()