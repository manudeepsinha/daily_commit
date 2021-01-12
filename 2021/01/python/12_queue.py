'''
the following code is of queue and if I add some new methods to the class
i'll post in a what's new section.

what's new:
            Queue class with following methods:
                add
                add_all
                pop
                pop_all
                print_que
                check_empty

pending:    
            
'''
class Queue:

    def __init__ (self):
        self.queue = []

    def add (self,val):
        if val not in self.queue:
            self.queue.insert(0,val)
            print(f'{val} is added in the queue.')
            return
        print(f'{val} is already in the queue.')
        return

    def add_all (self):
        que = input("Enter the elements space seperated: ")
        que = que.split()
        count = 0
        for item in que:
            self.queue.append(item)
            count += 1
        print(f"Added {count} elements in the queue.")
        return

    def pop (self):
        if self.check_empty():
            return
        print(f'Popped item is: {self.queue.pop()}')
        return

    def pop_all (self):
        if self.check_empty():
            return
        iterate = len(self.queue)
        for item in range(iterate):
            self.queue.pop()
        return

    def print_que (self):
        if self.check_empty():
            return
        print(self.queue[::-1])
        return

    def check_empty (self):
        if len(self.queue) == 0:
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