#题目：定义栈的数据结构，请在该类型中实现一个能够得到栈中所含最小元素的min函数。
class Stack:
    def __init__(self):
        self.stack = []

    def push(self,val):
        self.stack.append(val)

    def pop(self):
        self.stack.pop()

    def min(self):
        return min(self.stack)

if __name__ == '__main__':
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    print(stack.min())
