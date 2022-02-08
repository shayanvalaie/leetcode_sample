""" 
Leetcode 2. Add Two Numbers

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        dummy = ListNode()  # Create a dummy node which will be the head of the list we return
        curr = dummy  # Init current pointer as our dummy node
        carry = 0  # Init a carry variable when we need to count numbers that exceed 10

        while l1 or l2 or carry:  # While there are values in l1, l2, or carry.
            # Add the number
            # V1 starts as the first value of l1 if there is a val else it is 0
            v1 = l1.val if l1 else 0
            # V2 starts as the first value of l2 if there is a val else it is 0
            v2 = l2.val if l2 else 0

            val = v1 + v2 + carry  # Our value is equal to v1 + v2 + our carry variable

            # Get the carry value
            # Carry will equal val divided and rounded down by 10 (If val is 15 carry = 1)
            carry = val // 10
            # Now that we have the carry out we want change val to the remainded (If val = 15 the remainder would be 5)
            val = val % 10
            # Now curr.next = a new node with the value of the remainder
            curr.next = ListNode(val)

            # Update pointers
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            curr = curr.next
        return dummy.next  # Return head of new list
