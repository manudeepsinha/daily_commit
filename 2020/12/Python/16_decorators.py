def new_decorator(some_func):

	def wrap_func():
		print('I am on top of the function!')

		some_func()

		print('I am below of the function')

		return wrap_func

def func_needs_decorator():

	print('I need some decorators!!!')


#Approach 1 to add new_decorator() with func_needs_decorator:

#Reassigning func_needs_decorator() as:
func_needs_decorator = new_decorator(func_needs_decorator)

#Then calling the function:
func_needs_decorator()


#------------------------------------------#

#Approach 2 is using decorator:
@new_decorator
def func_needs_decorator():

	print('I need some decorators!!!')


#Now just call the function:
func_needs_decorator()

'''Note that here we can use the decorator as switch. If we don't want to use, simply comment it out will work.'''