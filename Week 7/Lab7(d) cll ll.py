class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularQueue:
    def __init__(self):
        self.front = None
        self.rear = None

    # Enqueue
    def enqueue(self):
        value = int(input("Enter element: "))
        new_node = Node(value)

        if self.front is None:
            self.front = self.rear = new_node
            new_node.next = self.front
        else:
            new_node.next = self.front
            self.rear.next = new_node
            self.rear = new_node

        print("Element inserted.")

    # Dequeue
    def dequeue(self):
        if self.front is None:
            print("Queue is empty.")
            return

        print("Deleted element:", self.front.data)

        if self.front == self.rear:
            self.front = None
            self.rear = None
        else:
            self.front = self.front.next
            self.rear.next = self.front

    # Peek
    def peek(self):
        if self.front is None:
            print("Queue is empty.")
        else:
            print("Front element:", self.front.data)

    # Display
    def display(self):
        if self.front is None:
            print("Queue is empty.")
            return

        temp = self.front

        print("Queue elements:")

        while True:
            print(temp.data, end=" ")

            temp = temp.next

            if temp == self.front:
                break

        print()


# Main program
queue = CircularQueue()

while True:
    print("\n--- CIRCULAR QUEUE USING LINKED LIST ---")
    print("1. Enqueue")
    print("2. Dequeue")
    print("3. Peek")
    print("4. Display")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        queue.enqueue()

    elif choice == 2:
        queue.dequeue()

    elif choice == 3:
        queue.peek()

    elif choice == 4:
        queue.display()

    elif choice == 5:
        print("Program exited.")
        break

    else:
        print("Invalid choice.")
