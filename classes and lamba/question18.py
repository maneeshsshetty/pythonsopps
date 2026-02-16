def check_string(s):
    has_upper = any(c.isupper() for c in s)
    has_lower = any(c.islower() for c in s)
    has_digit = any(c.isdigit() for c in s)
    is_long_enough = len(s) >= 10
    
    if has_upper and has_lower and has_digit and is_long_enough:
        return "Valid String"
    else:
        return "Invalid String"

print(check_string("PAceWIsd0m"))
