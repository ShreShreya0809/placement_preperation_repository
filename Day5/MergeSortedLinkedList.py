class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def ins(self, new_value):
        temp = Node(new_value)
        if self.head is None:
            self.head = temp
            self.tail = temp    
            return
        self.tail.next = temp
        self.tail = temp

def p(n):
    while n is not None:
        print(n.value, end=' ')
        n = n.next
    print()

def fun(head1, head2):
    if head1 is None and head2 is None: return
    if head1 is None and head2 is not None: return head2
    if head1 is not None and head2 is None: return head1
    if head2.value < head1.value:
        temp = head1
        head1 = head2
        head2 = temp
    ans = head1
    while(head1 is not None and head2 is not None):
        temp = None
        while(head1 is not None and head1.value <= head2.value):
            temp = head1
            head1 = head1.next
        temp.next = head2
        t = head1
        head1 = head2
        head2 = t
    
    return ans

if __name__ == '__main__':
    for _ in range(int(input())):
        n, m = map(int, input().strip().split())
        
        a = LinkedList()
        b = LinkedList()
        na = list(map(int, input().strip().split()))
        nb = list(map(int, input().strip().split()))
        for x in na: a.ins(x)
        for x in nb: b.ins(x)
        
        p(fun(a.head, b.head))
