is_number = lambda s: s.replace('.', '', 1).isdigit() or (s.startswith('-') and s[1:].isdigit())

print(is_number('26587'))
print(is_number('4.2365'))
print(is_number('-12547'))
print(is_number('abc'))
