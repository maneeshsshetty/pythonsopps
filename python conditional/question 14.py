def print_multiplication_table(number):
    print(f"--- Multiplication Table of {number} ---")
    for i in range(1, 11):
        product = number * i
        print(f"{number} * {i:2} = {product}")
print(" ENter a number to get the multiplication table")
num=int(input())
print_multiplication_table(num)
