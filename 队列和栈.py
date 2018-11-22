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

#使用队列模拟栈
class StackByQueue(object):
    def __init__(self):
        self.queue = Queue()

    def push(self,val):
        return self.queue.enqueue(val)

    def pop(self):
        for i in range(self.queue.size()-1):
            value = self.queue.dequeue()
            self.queue.enqueue(value)
        return self.queue.dequeue()
#使用栈模拟队列
class QueueByStack(object):
    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()

    def enqueue(self,val):
        self.stack1.push(val)

    def dequeue(self):
        #pop出stack1里除了最开始以外的数至stack2里，res赋值为stack1里的那个数
        for i in range(self.stack1.size()-1):
            value = self.stack1.pop()
            self.stack2.push(value)
        res = self.stack1.pop()
        #再将stack2的数pop回stack1里，这样除了最开始的数，其余不变，实现先进先出
        for i in range(self.stack2.size()-1):
            value = self.stack2.pop()
            self.stack1.push(value)
        return res