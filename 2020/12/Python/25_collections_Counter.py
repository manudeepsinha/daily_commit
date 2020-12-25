#exploring Counter
from collections import Counter

#inserting test lists/inputs
nums = [1,2,1,2,2,3,3,4,3,4,3,1,2,3,4,5,5,6,7,8,8,8,7]
s = 'aasfbnjasnfjafbbanasdnfkaakfnvvavavav'
string = 'This string can be repeated and check repetition of word word what can be done to get repeated string yes string yes yes check that'
#making a list of words
words = string.split()


#1 printing frequency of each element
print('Prints the frequency of each number given in nums in dict format:\n', Counter(nums))
print('\n\nPrints the frequency of each alphabet given in s in dict format:\n', Counter(s))
print('\n\nPrints the frequency of each word given in string in dict format:\n', Counter(words))

#making Counter objects
on = Counter(nums)
os = Counter(s)
ostring = Counter(words)

#now working with some Counter methods

#2 printing most common element
print(f'\n\nMost occuring number is: {on.most_common(1)[0][0]} and occured {on.most_common(1)[0][1]} many times.')
print(f'\n\nMost occuring alphabet is: {os.most_common(1)[0][0]} and occured {os.most_common(1)[0][1]} many times.')
print(f'\n\nMost occuring word is: {ostring.most_common(1)[0][0]} and occured {ostring.most_common(1)[0][1]} many times.')

#3 printing least common element
print(f'\n\nLeast occuring number is: {on.most_common()[:-1-1:-1][0][0]} and occured {on.most_common()[:-1-1:-1][0][1]} many time(s).')
print(f'\n\nLeast occuring alphabet is: {os.most_common()[:-1-1:-1][0][0]} and occured {os.most_common()[:-1-1:-1][0][1]} many time(s).')
print(f'\n\nLeast occuring word is: {ostring.most_common()[:-1-1:-1][0][0]} and occured {ostring.most_common()[:-1-1:-1][0][1]} many time(s).')

#4 printing total enteries
print(f'\n\nTotal number of numbers are: {sum(on.values())}')
print(f'\n\nTotal number of alphabets are: {sum(os.values())}')
print(f'\n\nTotal number of words are: {sum(ostring.values())}')

#5 printing list of (elem, cnt) pairs
print('\n\n',on.items())
print('\n\n',os.items())
print('\n\n',ostring.items())

#6 converting back to dict
print('\n\n',Counter(dict(on.items())))
print('\n\n',Counter(dict(os.items())))
print('\n\n',Counter(dict(ostring.items())))