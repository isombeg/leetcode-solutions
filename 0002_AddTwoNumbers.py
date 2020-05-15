# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode(0)
        curr = head
        sum = l1.val + l2.val
        curr.val += sum % 10
        
        while l1.next != None and l2.next != None:
            # Establishing next least significant digit within sum
            curr.next = ListNode(1 if sum >= 10 else 0)
            curr = curr.next
            
            # Update l1 and l2
            l1, l2 = l1.next, l2.next
            
            # Update overall sum and curr
            sum = l1.val + l2.val + curr.val
            curr.val = sum % 10
            
        # Special case: First input has more digits than second input
        while l1.next != None:            
            # Accounting for carry over digit
            curr.next = ListNode(1 if sum >= 10 else 0)

            # Establishing next least significant digit within sum
            curr = curr.next
            
            # Update l1
            l1 = l1.next
            
            # Updating overall sum
            sum = l1.val + curr.val
            curr.val = sum % 10
            
        # Special case: Second input has more digits than first input
        while l2.next != None:
            
            # Accounting for carry over digit
            curr.next = ListNode(1 if sum >= 10 else 0)
            
            # Establishing next least significant digit within sum
            curr = curr.next
            
            # Update l2
            l2 = l2.next
            
            # Updating overall sum
            sum = l2.val + curr.val
            curr.val = sum % 10
            
        # Special case: Sum has more digits then the inputs
        if sum >= 10:
            curr.next = ListNode(1)
            
        return head
            