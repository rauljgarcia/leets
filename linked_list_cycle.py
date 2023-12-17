'''
Linked List Cycle

Given head, the head of a linked list determine if the linked
    list has a cycle in it.

There's a cycle in a linked list if there is some node in the
    list that can be reached again by continuously following
    the next pointer. 

Internally, pos is used to denote the index of the node that
    tail's next pointer is connected to. Note that pos is not
    passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.
'''
def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool

        Implementation results
        Runtime: 37ms
        Memory: 20.37ms
        """
        slow_ptr = head
        fast_ptr = head
        while fast_ptr is not None and fast_ptr.next is not None:
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next.next
            if fast_ptr == slow_ptr:
                return True
        return False