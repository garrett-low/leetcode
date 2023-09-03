# Given the head of a singly linked list and two integers left and right where left <= right, reverse the nodes of the list from position left to position right, and return the reversed list.

# to do: fix the pointers to the left - 1 and right + 1 node

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse(head, left, right):
    prev = None
    curr = head
    
    for i in range(right):
        if i >= left:
            next_node = curr.next
            curr.next = prev            
            prev = curr
            curr = next_node
        else:
            prev = curr
            curr = curr.next

    debug_print(head)
    return head

def debug_print(head):
    curr = head
    while curr:
        print(f"[{curr.val}]", end = '')
        curr = curr.next
    print()

test = ListNode(1)
test.next = ListNode(2)
test.next.next = ListNode(3)
test.next.next.next = ListNode(4)
test.next.next.next.next = ListNode(5)
test.next.next.next.next.next = ListNode(6)
reverse(test, 2, 4)