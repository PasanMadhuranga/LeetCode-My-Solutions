# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Recursive solution
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if (not head):
            return head

        if (not head.next):
            return head

        first = head
        head = head.next
        first.next = self.swapPairs(head.next)
        head.next = first
        return head
        


# Another solution found in the discussion section
# Iterative solution
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if (not head or not head.next):
            return head
        
        dummy = ListNode(0, head)
        prev = dummy
        cur = head

        while(cur and cur.next):
            prev.next =cur.next
            cur.next = cur.next.next
            prev.next.next = cur
            prev = cur
            cur = cur.next
        
        return dummy.next
        