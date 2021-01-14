'''
the following code is built on the wip binary tree code.
i'll post the entire code everytime i make new addition of code with this line at top and 
a what's new section.

what's new:
            insert
            find
            print_tree
			
pending:
'''

class BTree:
	def __init__ (self,data):

		self.left = None
		self.right = None
		self.data = data

	def insert (self,data):
		if self.data:
			if data < self.data:
				if self.left is None:
					self.left = BTree(data)
				else:
					self.left.insert(data)
			elif data > self.data:
				if self.right is None:
					self.right = BTree(data)
				else:
					self.right.insert(data)
		else:
			self.data = data

	def find (self, val):
		if val < self.data:
			if self.left is None:
				return str(val) + " Not Found!"
			return self.left.find(val)
		elif val > self.data:
			if self.right is None:
				return str(val) + "Not Found!"
			return self.right.find(val)
		else:
			print(str(self.data) + " is Found!")


	def print_tree (self):
		if self.left:
			self.left.print_tree()
		print(self.data)
		if self.right:
			self.right.print_tree()

#test code to run
root = BTree(5)

root.insert(1)
root.insert(3)
root.insert(6)
root.insert(12)

root.print_tree()

root.find(12)
root.find(2)