def replace_not_poor(s):
    not_pos = s.find('not')
    poor_pos = s.find('poor')
    if not_pos != -1 and poor_pos != -1 and not_pos < poor_pos:
        result = s[:not_pos] + 'good' + s[poor_pos + 4:]
        return result
    return s
s1 = 'The lyrics is not that poor!'
print(f"Input: '{s1}'")
print(f"Output: '{replace_not_poor(s1)}'")
print()
s2 = 'The lyrics is poor!'
print(f"Input: '{s2}'")
print(f"Output: '{replace_not_poor(s2)}'")
