# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        dummy = ListNode()
        tail = dummy

        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            
            ## will evaluate when list 1 and list 2 are equal
            ## when equal condition, we want our pointer to point at the end of the list2
            ## because we are going from head -> l1 -> l2 
            else:
                tail.next = list2
                list2 = list2.next

            tail = tail.next

        # if list 1 or list 2 are still pending elements
    
        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2

        return dummy.next

## T(C) : O(max(n,m))
## S(C) : O(1)




        
