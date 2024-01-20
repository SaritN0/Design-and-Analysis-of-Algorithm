class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)
        print(f"{item} pushed to the stack")

    def pop(self):
        if not self.is_empty():
            popped_item = self.items.pop()
            print(f"{popped_item} popped from the stack")
            return popped_item
        else:
            print("Stack is empty")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            print("Stack is empty")

    def display(self):
        print("Stack:", self.items)


stack = Stack()

while True:
    print("\nStack Operations:")
    print("1. Push")
    print("2. Pop")
    print("3. Peek")
    print("4. Display")
    print("5. Quit")

    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        item = input("Enter the element to push: ")
        stack.push(item)
    elif choice == '2':
        stack.pop()
    elif choice == '3':
        peek_item = stack.peek()
        if peek_item is not None:
            print("Top element:", peek_item)
    elif choice == '4':
        stack.display()
    elif choice == '5':
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please enter a valid option.")