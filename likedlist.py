class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete(self, key):
        current_node = self.head
        if current_node and current_node.data == key:
            self.head = current_node.next
            current_node = None
            return

        prev_node = None
        while current_node and current_node.data != key:
            prev_node = current_node
            current_node = current_node.next

        if current_node is None:
            print(f"{key} not found in the list.")
            return

        prev_node.next = current_node.next
        current_node = None

    def display(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=" -> ")
            current_node = current_node.next
        print("None")


# Create a linked list
linked_list = LinkedList()

while True:
    print("\nLinked List Operations:")
    print("1. Append")
    print("2. Prepend")
    print("3. Delete")
    print("4. Display")
    print("5. Quit")

    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        item = input("Enter the element to append: ")
        linked_list.append(item)
    elif choice == '2':
        item = input("Enter the element to prepend: ")
        linked_list.prepend(item)
    elif choice == '3':
        key = input("Enter the element to delete: ")
        linked_list.delete(key)
    elif choice == '4':
        linked_list.display()
    elif choice == '5':
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please enter a valid option.")