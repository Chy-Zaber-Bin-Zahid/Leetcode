class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev, cur = None, head
        while head.next != None:
            prev = head.next
            head.next = prev.next
            prev.next = cur
            cur = prev
            
        return prev

    # Helper function to convert a list to a linked list
def list_to_linkedlist(elements):
    dummy = ListNode(0)
    current = dummy
    for element in elements:
        current.next = ListNode(element)
        current = current.next
    return dummy.next


# Testing the solution
sol = Solution()
linked_list = list_to_linkedlist([0, 1, 3, 4])
print(sol.reverseList(linked_list))