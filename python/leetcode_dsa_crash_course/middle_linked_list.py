# Given the head of a singly linked list, return the middle node of the linked list.
# If there are two middle nodes, return the second middle node.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def middleNode(head):
    fast = head
    slow = head
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    print(slow.val)
    return slow.val

test = ListNode(1)
test.next = ListNode(2)
test.next.next = ListNode(3)
test.next.next.next = ListNode(4)
test.next.next.next.next = ListNode(5)
middleNode(test)
test.next.next.next.next.next = ListNode(6)
middleNode(test)