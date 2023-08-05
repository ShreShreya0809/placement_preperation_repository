class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        LL= ListNode(None)
        temp,a,b= LL,0,0
        while(l1 is not None or l2 is not None or b != 0):
            a=0
            if l1:
                a+=l1.val
                l1=l1.next
            if l2:
                a+=l2.val
                l2=l2.next
            a+=b
            b=a//10
            node=ListNode(a % 10)
            temp.next=node
            temp=temp.next
        return LL.next
