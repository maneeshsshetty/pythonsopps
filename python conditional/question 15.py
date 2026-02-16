numbers = []
total_sum = 0
product = 1
while True:
    user_input = input("Enter an integer (or 'q' to quit): ")
    if user_input.lower() == 'q':
        break
    else:
        try:
            number = int(user_input)
            numbers.append(number)
            total_sum += number
            product *= number
        except ValueError:
            print("Invalid input! Please enter a valid integer or 'q'.")
if numbers:
    average = total_sum / len(numbers)
    print("\n--- Results ---")
    print(f"Numbers entered: {numbers}")
    print(f"Average of all numbers: {average:.2f}")
    print(f"Product of all numbers: {product}")
else:
    print("\nNo numbers were entered.")

