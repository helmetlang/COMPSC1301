name = input()
# replace is a string method
user_name = name.replace(" ", "")

if str(user_name) == str(user_name)[::-1]:
# [::-1] is slice notation for lists, which basically just means
# <object_name>[<start_index>, <stop_index>, <step>]
# starts from the end towards the first taking each element.
# https://stackoverflow.com/questions/31633635/what-is-the-meaning-of-inta-1-in-python
    
    print(name + " is a palindrome")
else:
    
    print(name + " is not a palindrome")
    
# However in the zybooks submission, the problem is for strings larger than one word, does not
# Correctly give if it is a palindrome or not