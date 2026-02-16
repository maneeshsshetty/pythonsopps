def main():
    try:
        n = int(input("How many items will the list have? "))
    except ValueError:
        print("Invalid number. Exiting.")
        return

    items = []
    for i in range(1, n + 1):
        items.append(input(f"Enter item {i}: "))

    target = input("Enter the item to search and delete: ")

    if target in items:
        items.remove(target)
        print(f"'{target}' found and deleted.")
    else:
        print(f"'{target}' not found in the list.")

    print("Final list (iterated with a for loop):")
    for it in items:
        print(it)


if __name__ == '__main__':
    main()