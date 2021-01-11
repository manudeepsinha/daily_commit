'''
the following code is built on the wip linked list code and adding some methods to the class
i'll post the entire code everytime i make new addition of code with this line at top and 
a what's new section.

what's new:
            finding an element
            deletion method
            inserting multiple elements
            deleting all elements
			

pending:    length of list
			deletion in middle with optional argument of previous value
			populating the linked list using method that keep on asking for user input
			usage of other approaches for insertion/deletion for improved effeciency
'''


#building linked list in this block

class LLNode:
    def __init__ (self,val = None):
        self.data = val
        self.next = None
        
class LinkedList:
    def __init__ (self):
        self.head = None
        self.length = 0
    
''' def menu (self): or can be included in __init__ 
       print('This linked list can perform multiple operations')
       print('Print all elements in the list using print_ll') 
       print('Add an element at start using add_at_start') 
       print('Add an element at end using add_at_last') 
       print('Remove an element at start using remove_at_start') 
       print('Remove an element at end using remove_at_end') 
       print('Check whether an element in a list or not using find') '''
        
    def print_ll (self):
        if not self.head:
            print('Empty List!')
            return
        start = self.head 
        while start is not None:
            print(start.data)
            start = start.next

    #working, figuring out to print int as it's not callable
''' def length (self):
        print("The length of the given LinkedList is: ")
        return self.length '''
            

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

    def add_at_middle (self,before_node,node):
        #when list is empty
        if self.head == None:
            print("Empty List!\nAdding the element at the start.")
            self.add_at_last(node)
            return

        start = self.head
        while start.next is not None:
            if start.data == before_node:
                break
            start = start.next
        if start.data != before_node:
            print("Data not found!")
            return
        new_node = LLNode(node)
        new_node.next = start.next
        start.next = new_node
        self.length += 1

    def add_multiple (self):
        ip_list = input('Enter space seperated elements: ')
        ip_list = ip_list.split()
        for item in ip_list:
            self.add_at_last(item)
            self.length += 1

    def delete_all (self):
        self.head = None
        self.length = 0
    

    def remove_at_start (self):
        if self.head == None:
            print('Empty List!')
            return
        else:
            to_remove = self.head
            self.head = self.head.next
            to_remove.next = None
            self.length -= 1
            return 
        
    
    def remove_at_end (self):
        if self.head == None:
            print('Empty list!')
            return
        
        if self.head.next == None:
            self.head = None
            self.length -= 1
            return
        
        start = self.head
        pre_to_start = None
        
        while start.next is not None:
            pre_to_start = start
            start = start.next
        pre_to_start.next = None
        self.length -= 1
        return

    #working  
    def remove_at_middle (self, node): #before_node = None
        if self.head == None:
            print("Empty List!")
            return

        #to-do:
    ''' if before_node != None:
            start = self.head
            pre_to_start = None
            while start.next is not None:
                pre_to_start = start
                start = start.next '''
        if self.head.next == None:
            print("List has only one element.\nDeleting the item.\nList is now empty")
            self.head = None
            return
        start = self.head
        pre_to_start = None
        count = 0
        if start.data == node:
            self.remove_at_start()
            self.length -= 1
            return
        else:
            while start.next is not None:
                if start.data == node:
                    pre_to_start.next = start.next
                    count = 1
                    break
                pre_to_start = start
                start = start.next
        if count == 1:
            self.length -= 1
        else:
            if start.data == node:
                pre_to_start.next = None
                self.length -= 1
                return

    
  
    def find (self, val):        
        start = self.head
        if not start:
            print('Empty list!')
        else:
            while start is not None:
                if start.data == val:
                    print('Data Found!')
                    return 
                else:
                    start = start.next
            print('Data not found')
            return

    

#Test code to try exceptions as well
my_test = LinkedList()

my_test.print_ll()

my_test.add_at_start(20)
my_test.add_at_start(10)

my_test.add_at_last(30)
my_test.add_at_last(40)

my_test.print_ll()

my_test.remove_at_end()
my_test.print_ll()

my_test.remove_at_start()
my_test.print_ll()

my_test.remove_at_start()
my_test.print_ll()

my_test.remove_at_end()
my_test.print_ll()

#Now that the list is empty
my_test.remove_at_end()
my_test.remove_at_start()

#Adding multiple elements
my_test.add_multiple()
#now writing elements seperated by space
my_test.print_ll()

#deleting all elements
my_test.delete_all()
my_test.print_ll()