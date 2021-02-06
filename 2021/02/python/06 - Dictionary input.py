#basic input of dictionary in python
n = int(input("Enter the number of input for the dictionary keys:"))
d = dict(input('\nEnter the key then value space seperated:').split() for _ in range(n))
print(f'\nDictionary is: {d}')