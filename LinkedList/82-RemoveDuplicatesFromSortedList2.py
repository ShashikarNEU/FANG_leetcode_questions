# Diffcult Problem
# Use dummy node and compare two nodes at once(2 cases- if they are same or not same)
# Dummy node thinking(we attach the dummy node to the list in the beggining and comsider the whole list as one) [Instead of adding nodes one by one to dummy node]
# Do Dry runs and draw it with Ipad to get the logic fast.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head):
        dummy = ListNode(-1)
        prev = dummy
        dummy.next = head
        if not head:
            return head

        curr = head

        while curr and curr.next:
            if curr.val != curr.next.val:
                prev = curr
                curr = curr.next    
            else:
                while curr.next and curr.val == curr.next.val:
                    curr = curr.next
                prev.next = curr.next
                curr = curr.next
        
        return dummy.next  