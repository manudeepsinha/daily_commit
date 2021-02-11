import re

text_to_search = '''
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890
Ha HaHa
MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )
coreyms.com
321-555-4321
123.555.1234
123*555*1234
800-555-1234
900-555-1234
Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T
'''

sentence = 'Start a sentence and then bring it to an end'

number = re.compile(r'\d{3}[-.]\d{3}[.-]\d{4}')
people = re.compile(r'Mr(r|s|rs)\.?\s[A-Z]\w*')
matches = people.finditer(text_to_search)

for match in matches:
    print(match)

count = 0
with open('data.txt','r',encoding = 'utf-8') as f:

	contents = f.read()

	matches = number.finditer(contents)

	for match in matches:
		print(match)
		count += 1
	print(f'There are {count} valid phone-numbers.')