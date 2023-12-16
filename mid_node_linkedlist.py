'''
876. Middle of the Linked List
Given the head of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node.
'''
def middleNode(self, head):
        '''
        Runtime
        16ms
        Beats 44.65% of users with Python
        Memory
        13.28 MB 
        Beats 66.73% of users with Python
        '''
        slow_ptr = head
        fast_ptr = head
        while fast_ptr is not None and fast_ptr.next is not None:
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next.next
        return slow_ptr