class Solution:
    def deleteNode(self,curr_node):
        if curr_node.next is not None:
            curr_node.data = curr_node.next.data
            curr_node.next = curr_node.next.next
            return curr_node
        return
