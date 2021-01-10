'''
the following code is built on the wip linked list code and adding some methods to the class
i'll post the entire code everytime i make new addition of code with this line at top and 
a what's new section.

what's new:
			menu of methods (commented in the class LinkedList)
			print method
			insertion method (at beginning, at ending)

pending:
			insetion at middle
			deletion method
			finding an element
			populating the linked list using method that keep on asking for user input
			usage of other approaches for insertion/deletion for improved effeciency
'''

class LLNode:
    def __init__ (self,val = None):
        self.data = val
        self.next = None
        
class LinkedList:
    def __init__ (self):
        self.head = None
        self.length = 0
    
   #def menu (self): or can be included in __init__
     #  print('This linked list can perform multiple operations')
     #  print('Print all elements in the list using print_ll') 
     #  print('Add an element at start using add_at_start') 
     #  print('Add an element at end using add_at_last') 
     #  print('Remove an element at start using remove_at_start') 
     #  print('Remove an element at end using remove_at_end') 
     #  print('Check whether an element in a list or not using find') 
     
    def print_ll (self):
        if not self.head:
            print('Empty List!')
            return
        start = self.head 
        while start is not None:
            print(start.data)
            start = start.next
            

    def add_at_start (self,node):
        new_node = LLNode(node)
        self.length += 1
        new_node.next = self.head
        self.head = new_node
  
  
    def add_at_last (self,node):
        if self.length != 0:
            new_node = LLNode(node)
            end = self.head
            while end.next is not None:
                end = end.next
            end.next = new_node
            new_node.next = None
        else:
            self.add_at_start(node)
            
        self.length += 1
        


#Test code as follows:

my_test = LinkedList()

my_test.print_ll()

my_test.add_at_start(20)
my_test.add_at_start(10)

my_test.add_at_last(30)
my_test.add_at_last(40)

my_test.print_ll()