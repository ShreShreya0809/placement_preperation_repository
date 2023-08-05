def removeKthNode(head, k):
    if(k==0): return head
    temp=Node(-1)
    temp.next=head
    ptr1,ptr2=temp,temp
    for i in range(k):
        if(ptr2.next is None): return
        ptr2=ptr2.next
    while(ptr2.next is not None):
        ptr1=ptr1.next
        ptr2=ptr2.next
    if(ptr1==temp): return head.next
    ptr1.next=ptr1.next.next
    return head
