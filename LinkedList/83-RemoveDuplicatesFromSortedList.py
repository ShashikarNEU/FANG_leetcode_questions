# Follow dummy node lgic comparing new list and t1, check if it's same. if not, add it else, skip it
# EDGE CASE: After it ends, Do prev.next = None to cut off any duplicates at the end

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head):
        dummy = ListNode(-1)
        prev = dummy
        if not head:
            return head
        t1 = head
        prev.next = t1
        prev = t1
        t1 = t1.next

        while t1:
            if prev.val != t1.val:
                prev.next = t1
                prev = t1
    
            t1 = t1.next
        # EDGE CASE
        prev.next = None
        return dummy.next

# Given Soln(Cleaner code!!)
class Solution:
    def deleteDuplicates(self, head):
        # Start a pointer at the beginning of the list
        current = head
        
        # Traverse as long as the current node and the next one exist
        while current and current.next:
            # If the next node is a duplicate...
            if current.val == current.next.val:
                # ...skip it by pointing to the one after it.
                current.next = current.next.next
            else:
                # ...otherwise, just move to the next node.
                current = current.next
                
        return head