# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:

        superhead = ListNode(0, head)
        prefixsum = 0
        prefix_lookup = {0: superhead}

        while head:
            prefixsum += head.val
            prefix_lookup[prefixsum] = head
            head = head.next

        head = superhead
        prefixsum = 0
        while head:
            prefixsum += head.val
            head.next = prefix_lookup[prefixsum].next
            head = head.next

        return superhead.next
