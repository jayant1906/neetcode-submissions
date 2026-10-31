# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head.next is None:
            if n == 1:
                head = None
                return head
            else:
                return head
        
        start = head
        counter = 1
        while start.next:
            counter += 1
            start = start.next
        node_to_remove = counter - n

        start_2 = head
        if node_to_remove == 0:
            temp = head.next
            head.next = None
            head = temp
            return head
        while node_to_remove != 0:
            node_to_remove -= 1
            if node_to_remove == 0:
                tmp = start_2.next.next
                start_2.next.next = None
                start_2.next = tmp
                break
            start_2 = start_2.next

        return head
        
        




        