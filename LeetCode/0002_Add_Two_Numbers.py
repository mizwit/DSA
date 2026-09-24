# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = False
        empty = ListNode()

        sum = l1.val + l2.val
        if carry:
            sum += 1
        if sum > 9:
            sum = sum % 10
            carry = True
        else:
            carry = False
            
        result = ListNode(sum)
        current = result

        while True:
            l1 = l1.next if l1.next else empty
            l2 = l2.next if l2.next else empty

            if l1 == l2 and not carry:
                break
            
            sum = l1.val + l2.val
            if carry:
                sum += 1
            if sum > 9:
                sum = sum % 10
                carry = True
            else:
                carry = False

            current.next = ListNode(sum)
            current = current.next
        
        return result   