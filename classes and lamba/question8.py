class StringManipulator:
    def __init__(self):
        self.text = ""
    def get_string(self):
        self.text = input("Enter a string: ")
    def print_string(self):
        print("Reversed string:", self.text[::-1])
obj = StringManipulator()
obj.get_string()
obj.print_string()
