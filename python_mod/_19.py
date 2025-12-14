class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        
        dummy = ListNode(0, head)
        fast = dummy
        slow = dummy
        
        for _ in range(n + 1):
            if not fast:
                return head
            fast = fast.next
            
        while fast:
            fast = fast.next
            slow = slow.next
            
        slow.next = slow.next.next
        
        return dummy.next
    
# --- Helper function for list creation and printing ---

def create_linked_list(arr: list[int]) -> ListNode | None:
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

def print_linked_list(head: ListNode | None):
    if not head:
        return "[]"
    
    nodes = []
    current = head
    while current:
        nodes.append(str(current.val))
        current = current.next
    return "[" + " -> ".join(nodes) + "]"
