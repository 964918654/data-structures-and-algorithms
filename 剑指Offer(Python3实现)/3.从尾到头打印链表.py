# 题目：输入一个链表，按链表值从尾到头的顺序返回一个ArrayList。

# 思路：将链表中的值记录到list之中，然后进行翻转list。
class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None