# 题目：输入一个链表，按链表值从尾到头的顺序返回一个ArrayList。

# 思路：将链表中的值记录到list之中，然后进行翻转list。
class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None


#解法1
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
class Solution:
    def reverselist(self,head):
        dummy = head
        tmp = dummy
        while head and head.next != None:
            dummy = head.next
            head.next = dummy.next
            dummy.next = tmp
            tmp = dummy

        return dummy

solution = Solution()
relist = solution.reverselist(head)
list = []
while relist:
    list.append(relist.val)
    relist = relist.next
print(list)

#解法2
head1 = ListNode(1)
head1.next = ListNode(2)
head1.next.next = ListNode(3)
head1.next.next.next = ListNode(4)
head1.next.next.next.next = ListNode(5)
class Solution2:
    def printlist(self,listNode):
        l = []
        while listNode:
            l.append(listNode.val)
            listNode = listNode.next
        return l[::-1]
solution2 = Solution2()
list2 = solution2.printlist(head1)
print(list2)


