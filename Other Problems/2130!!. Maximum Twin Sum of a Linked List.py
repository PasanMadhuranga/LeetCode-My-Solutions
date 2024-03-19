# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        travelNode = head
        numList = []
        n = 0
        while (travelNode):
            numList.append(travelNode.val)
            travelNode = travelNode.next
            n += 1
        
        maxTwinSum = 0
        for i in range(n//2):
            newTwinSum = numList[i] + numList[n-1-i]
            if (newTwinSum > maxTwinSum):
                maxTwinSum = newTwinSum
        
        return maxTwinSum


# Another solution found in the discussion section
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:        
        # Reverse first half of list while iterating to middle
        slow = fast = head
        prev = None
        while fast and fast.next:
            fast = fast.next.next
            slow.next, prev, slow = prev, slow, slow.next

        # Iterate over twin nodes
        max_sum = 0
        backward, forward = prev, slow

        while forward:
            max_sum = max(max_sum, backward.val + forward.val)
            forward = forward.next
            backward = backward.next
        return max_sum