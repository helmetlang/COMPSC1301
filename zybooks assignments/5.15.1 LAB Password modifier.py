word = input()
password = ''

user_input = input()
string_append = "q*s"

user_input = (user_input.replace('i', '!').replace('a','@')
              .replace('m', 'M').replace('B', '8').replace('o','.'))

print(user_input + string_append)