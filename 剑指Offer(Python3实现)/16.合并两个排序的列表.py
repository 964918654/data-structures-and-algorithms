'''
题目：输入两个单调递增的链表，输出两个链表合成后的链表，当然我们需要合成后的链表满足单调不减规则。

题解：将两个链表之中的数值转换到列表之中，并进行排序，将排序后的列表构造成链表。
'''
class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None

class Solution:
    def Merge(self,head1,head2):
        if head1 == None and head2 == None:
            return None
        num1,num2 =[],[]
        while head1:
            num1.append(head1.val)
            head1 = head1.next
        while head2:
            num2.append(head2.val)
            head2 = head2.next
        num = num1 + num2
        num.sort()
        print(num)
        head = ListNode(num[0])
        pre = head
        for i in range(1,len(num)):
            pre.next = ListNode(num[i])
            pre = pre.next
        return head

if __name__=='__main__':
    solution=Solution()
    pHead1_1 = ListNode(1)
    pHead1_2 = ListNode(3)
    pHead1_3 = ListNode(5)
    pHead1_1.next=pHead1_2
    pHead1_2.next=pHead1_3

    pHead2_1 = ListNode(2)
    pHead2_2 = ListNode(4)
    pHead2_3 = ListNode(6)
    pHead2_1.next=pHead2_2
    pHead2_2.next=pHead2_3
    ans=solution.Merge(pHead1_1,pHead2_1)
    print(ans.val)
    print(ans.next.val)
    print(ans.next.next.next.next.val)
