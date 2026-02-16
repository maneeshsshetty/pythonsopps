salary = float(input("Enter your salary: "))
year_of_service = float(input("Enter years of service: "))
if year_of_service > 5:
    bonus = 0.05 * salary
    print("Congratulations! You are eligible for a 5% bonus.")
    print("Net bonus amount:", bonus)
else:
    print("No bonus. You need more than 5 years of service.")
