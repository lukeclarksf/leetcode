class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head: ListNode | None, k: int) -> ListNode | None:
        
        dummy = ListNode(0, head)
        prev_group_tail = dummy
        
        while True:
            kth = head
            for _ in range(k - 1):
                if not kth:
                    break
                kth = kth.next
            
            if not kth:
                break
                
            next_group_head = kth.next
            
            curr, prev = head, next_group_head
            for _ in range(k):
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
                
            prev_group_tail.next = prev
            prev_group_tail = head
            head = next_group_head
            
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
