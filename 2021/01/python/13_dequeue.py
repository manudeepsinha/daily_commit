'''
the following code is of queue and if I add some new methods to the class
i'll post in a what's new section.

what's new:
            Dequeue class with following methods:
                add
                pop
                pop_all
                print_dq
                check_empty

pending:    
            right now it doesn't ask position. can do default insert(0,val) or similar approach.
    def add_all (self):
        que = input("Enter the elements space seperated: ")
        que = que.split()
        count = 0
        for item in que:
            self.dq.append(item)
            count += 1
        print(f"Added {count} elements in the queue.")
        return

'''
class Dequeue:

    def __init__ (self):
        self.dq = []

    def add (self,val,position=None):
        if not position:
            position = input(f'Enter a position where you want to insert {val}: (s for starting/ e for ending)')
        if val not in self.dq:
            if position.lower() == 's':
                self.dq.insert(0,val)
                print(f'{val} is added at the start of the queue.')
                return
            elif position.lower() == 'e':
                self.dq.append(val)
                print(f'{val} is added at the end of the queue.')
                return
            print("Invalid position.")
            return
        print(f'{val} is already in the queue.')
        return


    def pop (self,position=None):
        if self.check_empty():
            return
        if not position:
            position = input("Enter a position from where you want to delete the element: (s for starting/ e for ending)")
        if position.lower() == 's':
               print(f'Popped item is: {self.dq.pop(0)}')
                return
        elif position.lower() == 'e':
            print(f'Popped item is: {self.dq.pop()}')
            return
        print("Invalid position.")
        return

    def pop_all (self):
        if self.check_empty():
            return
        iterate = len(self.dq)
        for item in range(iterate):
            self.dq.pop()
        return

    def print_dq (self):
        if self.check_empty():
            return
        print(self.dq[])
        return

    def check_empty (self):
        if len(self.dq) == 0:
            print("Queue is empty!\nAdd some elements using add method.")
            return True
        return False

#test code
my_que = Queue()

my_que.add(40)
my_que.add(30)
my_que.add(20)
my_que.add(10)

my_que.print_que()

my_que.pop()
my_que.pop()
my_que.pop()
my_que.pop()

my_que.pop()
my_que.check_empty()

my_que.add_all()
my_que.print_que()
my_que.pop_all()
my_que.print_que()