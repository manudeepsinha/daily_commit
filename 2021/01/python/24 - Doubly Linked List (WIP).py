''' I've been understanding the working on doubly linked list and making tweaks in my BTree
    code as something was very wrong with the code I committed. Didn't get the time to write
    the whole code so uploading WIP part. I will rectify this behavior.
'''
class DLLNode:
    def __init__(self, data = None, next = None, pre = None):
        self.data = data
        self.next = next
        self.pre  = pre
        
class DLL:
    def __init__(self):
        self.head = None
    
    def push (self, node):
        new_node = DLLNode(data = node)
        new_node.next = head.next
        
        #wip
        #if self.head is not None:
        #    new_node
    def addEnd (self, node):
        pass