# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        dummy = ListNode(0)
        tail=dummy
        curr1=l1
        curr2=l2
        while curr1 != None or curr2 != None:
            if curr1 is not None:
                val1 = curr1.val
            else:
                val1 = 0
            if curr2 is not None:
                val2 = curr2.val
            else:
                val2 = 0        
            add = val1+val2+carry
            carry = add //10
            digit = add%10
            tail.next=ListNode(digit)
            tail = tail.next
            if curr1 is not None:
                curr1=curr1.next
            if curr2 is not None:
                curr2=curr2.next
        if carry>0:
            tail.next=ListNode(carry)
        return dummy.next


