# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        num1, num2 = "", ""
        temp1 = l1
        temp2 = l2
        while temp1 or temp2:
            if not temp1:
                num2 += str(temp2.val)
                temp2 = temp2.next
                continue
            if not temp2:
                num1 += str(temp1.val)
                temp1 = temp1.next
                continue
            num1 += str(temp1.val)
            num2 += str(temp2.val)
            temp1 = temp1.next
            temp2 = temp2.next
        num1, num2 = int(num1[::-1]), int(num2[::-1])
        final = str(num1 + num2)[::-1]
        temp = l1
        prev = None
        for i in final:
            if not temp:
                temp = prev
                temp.next = ListNode(i)
                prev = temp.next
                temp = temp.next.next
                continue
            temp.val = i
            prev = temp
            temp = temp.next
        return l1