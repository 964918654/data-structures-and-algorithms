#题目：输入一个链表，反转链表后，输出新链表的表头。

class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None

class Solution:
    def ReverseList(self,head):
        dummy = head
        tmp = dummy
        while head and head.next != None:
            dummy = head.next
            head.next = dummy.next
            dummy.next = tmp
            tmp = dummy
        return dummy

if __name__ == '__main__':
    solution = Solution()
    p1 = ListNode(1)
    p2 = ListNode(2)
    p3 = ListNode(3)
    p4 = ListNode(4)
    p1.next = p2
    p2.next = p3
    p3.next = p4
    l = solution.ReverseList(p1)
    print(l.val)