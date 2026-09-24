# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        groupPrev = dummy
        
        while True:
            groupLast = groupPrev
            for _ in range(k):
                if not groupLast: break
                groupLast = groupLast.next
            if not groupLast: break

            groupNext = groupLast.next
            groupFirst = groupPrev.next

            prev, cur = groupFirst, groupFirst.next
            for _ in range(k - 1):
                nxt = cur.next
                cur.next = prev
                prev = cur
                cur = nxt

            groupPrev.next = groupLast
            groupPrev = groupFirst
            groupFirst.next = groupNext

        return dummy.next
    
# O(n) Memory Solution - Easier to understand:

# class Solution:
#     def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # res = ListNode()
        # tail = res
        # arr = []
        # i = k

        # while head:
        #     if i > 0:
        #         arr.append(head.val)
        #         head = head.next
        #         i -= 1
                
        #     else:
        #         arr.reverse()
        #         for node in arr:
        #             tail.next = ListNode()
        #             tail = tail.next
        #             tail.val = node
        #         arr = []
        #         i = k

        # if i == 0: arr.reverse()
        # for node in arr:
        #     tail.next = ListNode()
        #     tail = tail.next
        #     tail.val = node
        
        # return res.next