# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1
        dummy = temp = ListNode(0) 

        while list1 and list2:
            valOne, valTwo = list1.val, list2.val
            if valOne > valTwo:
                temp.next = list2
                list2 = list2.next
            else:
                temp.next = list1
                list1 = list1.next
            temp = temp.next
        if not list1:
            temp.next = list2
        if not list2:
            temp.next = list1
        return dummy.next
        