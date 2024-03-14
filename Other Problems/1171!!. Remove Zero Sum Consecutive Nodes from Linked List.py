# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        travelNode = head
        listArr= []
        n = 0
        while (travelNode):
            listArr.append(travelNode.val)
            travelNode = travelNode.next
            n += 1
        
        i = 0
        delIndices = []
        while (i < n):
            curSum = listArr[i]

            if (curSum == 0):
                delIndices.append(i)
                i += 1
                continue
            
            for j in range(i+1, n):
                curSum += listArr[j]
                if (curSum == 0):
                    delIndices += [d for d in range(i, j+1)]
                    i = j + 1
                    break
            else:
                i += 1

        if (not delIndices): return head

        answer = None
        del_i = len(delIndices) - 1
        for i in range(n-1, -1, -1):
            if (i == delIndices[del_i]):
                del_i -= 1
                continue
            temp = ListNode(listArr[i])
            temp.next = answer
            answer = temp
        
        return answer
    

# Anothe Solution found in the discussion section
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Create a dummy node that serves as the new head of the modified list,
        # which helps easily return the head of the updated list later.
        cur = dummy = ListNode(0)
        # Link the dummy node to the original head of the list.
        dummy.next = head
        # Initialize prefix sum to 0.
        prefix = 0
        # Use an ordered dictionary to keep track of prefix sums and their corresponding nodes.
        # This is important because it maintains the insertion order, which is crucial for deleting nodes.
        seen = collections.OrderedDict()
        
        # Traverse the list.
        while cur:
            # Update the prefix sum by adding the current node's value.
            prefix += cur.val
            # If this prefix sum has been seen before, it means the current segment of the list (from the last occurrence of this prefix sum to the current node) sums to zero and should be removed.
            node = seen.get(prefix, cur)
            # Remove all nodes seen after the last occurrence of this prefix sum because their cumulative effect led to a sum of zero.
            while prefix in seen:
                seen.popitem()
            # Record the current prefix sum and node. If this prefix sum is seen again, it will be updated to this new node.
            seen[prefix] = node
            # Link the last node before the zero-sum sequence directly to the node after the current node, effectively removing the zero-sum sequence.
            node.next = cur = cur.next
        # Return the next of dummy node, which is the head of the modified list.
        return dummy.next

        