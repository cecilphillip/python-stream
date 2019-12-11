from math import pi

# print(pi)
#other_value = 1010.21331
#print(f'The value of 🍕 is {other_value:5.5}')

# multi_line = (
#     'some stuff here '
#     'some more stuff there '
#     f'{pi} '
#     'some other stuff right here too'
# )

# print(multi_line)

# string_with_spaces = ">    some spaces, in the, middle    <"
# result = string_with_spaces.rstrip('<').lstrip('>').strip() #strip() rstrip() lstrip()
# print(result)

# result = string_with_spaces.replace(',', '')
# print(result)

string_with_formatter = 'Here is a string with {stuff} in it'
print(string_with_formatter.format(stuff='code') )


