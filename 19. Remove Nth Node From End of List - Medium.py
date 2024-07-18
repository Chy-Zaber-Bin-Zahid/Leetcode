# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        length = 0
        temp = head
        prev = None
        while temp:
            length+=1
            temp = temp.next
        temp = head 
        if length == 0:
            head = None
            return head
        idxRemove = (length - n)
        for i in range(idxRemove+1):
            if i == idxRemove:
                if prev == None:
                    head = head.next
                    temp.next = None
                    return head
                prev.next = temp.next
                temp = None
                return head
            prev = temp
            temp = temp.next


