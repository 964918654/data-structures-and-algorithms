class ListNode(object):
    def __init__(self,x):
        self.val = x
        self.next = None

#实例化
A = ListNode('first')
B = ListNode('second')
C = ListNode('third')

A.next = B
B.next = C

#形成一条链表
#'first' -> 'second' -> 'third'
#遍历链表
tmp = A
while tmp != None:
    print(tmp.val)
    tmp = tmp.next
#递归遍历链表
def listorder(head):
    if head:
        print(head.val)
        listorder(head.next)
listorder(A)

#反转链表
class Solution(object):
    def reverselist(self,head):
        dummy = head
        tmp = dummy

        while head and head.next != None:
            #每次循环后dummy的值+1，
            dummy = head.next
            #每次head.next的值+1，直到为None
            head.next = dummy.next
            #dummy已经为next，tmp是val，例：2.next = 1
            dummy.next = tmp
            #再将tmp改为与dummy相等
            tmp = dummy
        return  dummy

# dummy = 2
# 1.next = 3
# 2.next = 1
# tmp = 2

#dummy = 3
#2.next = 4
#4.next = 3
#tmp = 3
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

solution = Solution()
reverse_head = solution.reverselist(head)
while reverse_head:
    print(reverse_head.val)
    reverse_head = reverse_head.next