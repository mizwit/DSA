# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head.next: return
        left, right = ListNode(0, head), ListNode(0, head)
        ptr = 0 - n
        while True:
            if right.next == None: break
            ptr += 1
            if ptr > 0: left = left.next
            right = right.next
        if ptr <= 0: head = head.next
        else: left.next = left.next.next
        return head