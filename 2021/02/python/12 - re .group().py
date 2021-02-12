import re

emails = '''
CoreyMSchafer@gmail.com
corey.schafer@university.edu
corey-321-schafer@my-work.net
'''
urls = '''
https://www.google.com
http://coreyms.com
https://youtube.com
https://www.nasa.gov
'''

email = re.compile(r'[a-zA-Z0-9.-]+@[a-zA-Z-]+\.(com|edu|net)')
url = re.compile(r'https?://(www.)?(\w+)(\.\w+)')

matches = url.finditer(urls)

print('Printing domain names:\n')

for domain in matches:
    print(domain.group(2),end='')
    print(domain.group(3))

print('\n\nNow printing emails:\n')

matches = email.finditer(emails)

for match in matches:
    print(match.group(0))