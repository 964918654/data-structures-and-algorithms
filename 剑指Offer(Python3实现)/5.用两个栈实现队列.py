# 题目：用两个栈来实现一个队列，完成队列的Push和Pop操作。 队列中的元素为int类型。
#
# 题解：申请两个栈Stack1和Stack2，Stack1当作输入，pop出stack1里n-1个数至stack2，return出剩下的数，再将stack2的数pop至stack1

class Solution:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self,val):
        self.stack1.append(val)

    def pop(self):
        for i in range(len(self.stack1)-1):
            self.stack2.append(self.stack1.pop())
        res = self.stack1.pop()
        for i in range(len(self.stack2)):
            self.stack1.append(self.stack2.pop())
        return res

if __name__=='__main__':
    solution = Solution()
    solution.push(1)
    solution.push(2)
    solution.push(3)
    solution.push(4)
    print(solution.stack1)
    print(solution.pop())
    print(solution.pop())
    print(solution.stack1)