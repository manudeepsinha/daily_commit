#this code makes a linked list and traverses the list then prints it.

#this class will be used to made new nodes
class LLNode:
    def __init__ (self, val = None):
        self.data = val
        self.next = None

#this class is used to make linked list
class LinkedList(LLNode):
    def __init__(self):
        self.head = None
   

#now adding some elements in the linked list and linking the elements     
my_list = LinkedList()
my_list.head = LLNode(0)
node1 = LLNode(1)
node2 = LLNode(2)
my_list.head.next = node1
node1.next = node2

#traversing the linked list
print(f'first element: {my_list.head.data}')
start = my_list.head
while start is not None:
    print(start.data)
    start = start.next