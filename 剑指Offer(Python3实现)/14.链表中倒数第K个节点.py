'''
题目：输入一个链表，输出该链表中倒数第k个结点。

题解：反转链表，寻找第K个节点。
'''
class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None


class Solution:
    def findNodeList(self,head,k):
        dummy = head
        tmp = dummy
        while head and head.next != None:
            dummy = head.next
            head.next = dummy.next
            dummy.next = tmp
            tmp = dummy
        for i in range(1,k):
            dummy = dummy.next
        return dummy

if __name__=='__main__':
    solution=Solution()
    k=-11
    p1=ListNode(1)
    p2=ListNode(2)
    p3=ListNode(3)
    p4=ListNode(4)
    p1.next=p2
    p2.next=p3
    p3.next=p4

    ans=solution.findNodeList(p1,k)
    print(ans.val)
