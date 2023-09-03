# Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def delete_duplicates(head):
    if not head:
        return head
    
    debug_print(head)
    slow = head
    fast = head.next
    
    while fast:
        if slow.val == fast.val:
            while fast and slow.val == fast.val:
                fast = fast.next
            slow.next = fast
        else:
            slow = slow.next
            fast = fast.next
    
    debug_print(head)
    return head

def debug_print(head):
    curr = head
    while curr:
        print(f"[{curr.val}]", end = '')
        curr = curr.next
    print()

test = ListNode(1)
test.next = ListNode(1)
test.next.next = ListNode(2)
delete_duplicates(test)

test2 = ListNode(1)
test2.next = ListNode(1)
test2.next.next = ListNode(2)
test2.next.next.next = ListNode(3)
test2.next.next.next.next = ListNode(3)
# test2.next.next.next.next.next = ListNode(3)
delete_duplicates(test2)