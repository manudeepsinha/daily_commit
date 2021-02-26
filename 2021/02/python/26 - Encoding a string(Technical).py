#TCS NQT 2021-02-21 Question 2 encoding 
def encode(string):
    arr = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    hash_map = {}
    start = 0
    end   = len(arr) - 1
    ans = ''
    isComplete = True
    while start < len(arr):
        hash_map[arr[start]] = arr[end]
        start += 1
        end   -= 1
    for letter in string:
        if letter in hash_map:
            ans += hash_map[letter]
        else:
            isComplete = False
            break
    if isComplete:
        return ans
    else:
        return "Invalid input!"

#driver code:
string = input()
print(encode(string))