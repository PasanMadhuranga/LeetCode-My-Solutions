# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if (not list1):
            return list2
        
        if (not list2):
            return list1

        if (list1.val <= list2.val):
            travel1, travel2 = list1, list2
            returnList = list1
        else:
            travel1, travel2 = list2, list1
            returnList = list2

        while (travel1.next and travel2):
            print(travel1.val, travel2.val)
            if (travel1.val <= travel2.val < travel1.next.val):
                travel1.next = ListNode(travel2.val, travel1.next)
                travel2 = travel2.next
            travel1 = travel1.next
        
        if (travel2):
            travel1.next = travel2
        
        return returnList


# Another solution found in the discussion section
# Recursive solution
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if (not list1): return list2
        if (not list2): return list1

        if (list1.val < list2.val):
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        
        list2.next = self.mergeTwoLists(list1, list2.next)
        return list2
