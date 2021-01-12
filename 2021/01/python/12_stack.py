'''
the following code is of stack and if I add some new methods to the class
i'll post in a what's new section.

what's new:
            Stack class with following methods:
                push
                push_all
                pop
                pop_all
                top
                print_stk
                check_empty

pending:    
            
'''

class Stack:

    def __init__ (self):
        self.stack = []

    def push (self,val):
        if val not in self.stack:
            self.stack.append(val)
            print(f'{val} is pushed onto the stack.')
            return
        print(f'{val} is already in the stack.')
        return

    def push_all (self):
        stk = input("Enter the elements space seperated: ")
        stk = stk.split()
        count = 0
        for item in stk:
            self.stack.append(item)
            count += 1
        print(f"Added {count} elements in the stack.")
        return

    def pop (self):
        if self.check_empty():
            return
        print(f'Popped item is: {self.stack.pop()}')
        return

    def pop_all (self):
        if self.check_empty():
            return
        iterate = len(self.stack)
        for item in range(iterate):
            self.stack.pop()
        return

    def top (self):
        if self.check_empty():
            return
        return self.stack[-1]

    def print_stk (self):
        if self.check_empty():
            return
        print(self.stack[::-1])
        return


    def check_empty (self):
        if len(self.stack) == 0:
            print("Stack is empty!\nAdd some elements using push method.")
            return True
        return False

#test code
my_stk = Stack()

my_stk.push(40)
my_stk.push(30)
my_stk.push(20)
my_stk.push(10)

my_stk.print_stk()

my_stk.top()

my_stk.pop()
my_stk.pop()
my_stk.pop()
my_stk.pop()

my_stk.pop()
my_stk.check_empty()
my_stk.top()

my_stk.push_all()
my_stk.print_stk()
my_stk.pop_all()
my_stk.print_stk()