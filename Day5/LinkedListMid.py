class Solution:
    def findMid(self, head):
        if(head is None): return head
        if(head.next is None): return head.data
        ptr1,ptr2=head,head
        while(ptr2 is not None and ptr2.next is not None):
            ptr1=ptr1.next
            ptr2=ptr2.next.next
        return ptr1.data
