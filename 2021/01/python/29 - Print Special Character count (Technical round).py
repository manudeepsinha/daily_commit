'''
	The following question came in the technical coding round where for the input string, the output should generate
	an integer of the count of special characters present in the input string.
'''
string = input()
string = string.split()
special = 0
for i in range(len(string)):
    if not string[i].isalnum():
        special += 1
print(special)

'''
	test input string: aa a234bc@ sad$ hsagd^
	expected output: 3
	actual putput: 3
	explanation: the input string contains 3 special characters: @ $ ^
'''