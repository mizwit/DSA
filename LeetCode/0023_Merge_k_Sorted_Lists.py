# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def mergeTwoLists(list1, list2):
            dummy = ListNode()
            tail = dummy

            while list1 and list2:
                if list1.val < list2.val:
                    tail.next = list1
                    list1 = list1.next
                else:
                    tail.next = list2
                    list2 = list2.next
                tail = tail.next
                
            if list1: tail.next = list1
            if list2: tail.next = list2
            return dummy.next

        def merge(ls):
            length = len(ls)
            # base cases
            if length == 0: return
            if length == 1: return ls[0]

            # recursive case
            return mergeTwoLists(merge(ls[:length // 2]), merge(ls[length // 2:]))

        return merge(lists)