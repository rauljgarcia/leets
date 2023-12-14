'''
206. Reverse Linked List
Given the head of a singly linked list, reverse the list,
and return the reversed list.

Example:
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]
'''
def reverse(self, head):
        '''
        Implemntation 1, Iterative
        Runtime: 22ms, beats 28.51 python users
        Memory: 15.39ms, beats 32.59 python users
        '''
        curr = head
        pre = None
        next = None
        while curr is not None:
            next = curr.next
            curr.next = pre
            pre = curr
            curr = next
        head = pre
        return head 