class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)
        print(f"{item} enqueued to the queue")

    def dequeue(self):
        if not self.is_empty():
            removed_item = self.items.pop(0)
            print(f"{removed_item} dequeued from the queue")
            return removed_item
        else:
            print("Queue is empty")

    def front(self):
        if not self.is_empty():
            return self.items[0]
        else:
            print("Queue is empty")

    def size(self):
        return len(self.items)

    def display(self):
        print("Queue:", self.items)


# Create a queue
queue = Queue()

while True:
    print("\nQueue Operations:")
    print("1. Enqueue")
    print("2. Dequeue")
    print("3. Front")
    print("4. Size")
    print("5. Display")
    print("6. Quit")

    choice = input("Enter your choice (1-6): ")

    if choice == '1':
        item = input("Enter the element to enqueue: ")
        queue.enqueue(item)
    elif choice == '2':
        queue.dequeue()
    elif choice == '3':
        front_item = queue.front()
        if front_item is not None:
            print("Front element:", front_item)
    elif choice == '4':
        print("Size of the queue:", queue.size())
    elif choice == '5':
        queue.display()
    elif choice == '6':
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please enter a valid option.")