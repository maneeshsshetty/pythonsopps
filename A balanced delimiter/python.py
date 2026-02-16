def is_balanced(input_str):
    stack = []
    bracket_map = {')': '(', ']': '[', '}': '{'}
    for char in input_str:
        if char in bracket_map:
            top_element = stack.pop() if stack else '#'
            if bracket_map[char] != top_element:
                return False
        elif char in bracket_map.values(): 
            stack.append(char)
    return not stack


inputval = "{(((([{}]))))}"

print("Input:")
print(inputval)
print("Output:")
print(is_balanced(inputval))
