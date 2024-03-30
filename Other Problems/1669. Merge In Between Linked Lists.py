# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        removeNode = list1

        for i in range(a-1):
            removeNode = removeNode.next

        temp = removeNode.next
        removeNode.next = list2
        removeNode = temp

        for i in range(b-a):
            removeNode = removeNode.next
        
        list2End = list2
        while (list2End.next):
            list2End = list2End.next
        
        list2End.next = removeNode.next

        return list1



        