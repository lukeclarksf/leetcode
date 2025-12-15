# Definition for singly-linked list.
class ListNode:
    """
    Represents a node in a singly-linked list.

    A singly-linked list is a linear data structure where each element (node) 
    points to the next node in the sequence. This structure is commonly used
    to represent large numbers where digits are stored in reverse order.
    """
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    """
    Contains the method to add two numbers represented by linked lists.
    """
    def addTwoNumbers(self, l1, l2):
        """
        Adds two non-negative numbers represented as two singly-linked lists.

        The digits are stored in **reverse order** (the head is the 1's place), 
        and each node contains a single digit. The process simulates manual 
        addition, moving from the least significant digit to the most significant 
        digit while managing a carry. 

        The time complexity is $O(\max(L_1, L_2))$, where $L_1$ and $L_2$ are the 
        lengths of the input linked lists, as we traverse the lists once.

        Args:
            l1 (Optional[ListNode]): The head of the first linked list (number 1).
            l2 (Optional[ListNode]): The head of the second linked list (number 2).

        Returns:
            dummy_head (Optional[ListNode]): The head of a new linked list representing the sum 
                                of the two input numbers.

        Examples:
            >>> # l1: (2 -> 4 -> 3) which is 342
            >>> # l2: (5 -> 6 -> 4) which is 465
            >>> # Sum: 342 + 465 = 807
            >>> # Result linked list: (7 -> 0 -> 8)
            >>> l1 = create_linked_list([2, 4, 3])
            >>> l2 = create_linked_list([5, 6, 4])
            >>> result = Solution().addTwoNumbers(l1, l2)
            >>> linked_list_to_list(result)
            [7, 0, 8]
        """
        dummy_head = ListNode(0)
        current = dummy_head
        carry = 0

        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            total_sum = val1 + val2 + carry
            carry = total_sum // 10
            new_digit = total_sum % 10

            current.next = ListNode(new_digit)
            current = current.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy_head.next

