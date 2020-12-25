from collections import namedtuple

#namedtuple acts as a class, meaning you can use named indices just like methods
#creating a namedtuple Dog
Dog = namedtuple('Dog', 'age breed name')

#now creating some enteries in the Dog namedtuple
sam = Dog(age = 2, breed = 'Lab', name = 'Sammy')
leo = Dog(age = 4, breed = 'Husky', name = 'Leo')
pam = Dog(age = 3, breed = 'Ret', name = 'Pammy')

#now using some named indices as methods
print(f'Age of {sam.name} is {sam.age} and breed is {sam.breed}.')
print(f'\n\nAge of {leo.name} is {leo.age} and breed is {leo.breed}.')
print(f'\n\nAge of {pam.name} is {pam.age} and breed is {pam.breed}.')
print('\n\nAbove statements were printed using named indicies of the tuple.')

#if we know the index of the named indicies, we can still get the same result
print(f'\n\nName of pam is {pam[2]} done using index.')