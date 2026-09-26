class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.front = -1
        self.rear = -1

    # Enqueue operation
    def enqueue(self):
        value = int(input("Enter element: "))

        if (self.rear + 1) % self.size == self.front:
            print("Queue is full.")
            return

        if self.front == -1:
            self.front = 0

        self.rear = (self.rear + 1) % self.size
        self.queue[self.rear] = value

        print("Element inserted.")

    # Dequeue operation
    def dequeue(self):
        if self.front == -1:
            print("Queue is empty.")
            return

        print("Deleted element:", self.queue[self.front])

        if self.front == self.rear:
            self.front = -1
            self.rear = -1
        else:
            self.front = (self.front + 1) % self.size

    # Peek operation
    def peek(self):
        if self.front == -1:
            print("Queue is empty.")
        else:
            print("Front element:", self.queue[self.front])

    # Display operation
    def display(self):
        if self.front == -1:
            print("Queue is empty.")
            return

        print("Queue elements:")

        i = self.front

        while True:
            print(self.queue[i], end=" ")
            
            if i == self.rear:
                break

            i = (i + 1) % self.size

        print()


# Main program
size = int(input("Enter queue size: "))
queue = CircularQueue(size)

while True:
    print("\n--- CIRCULAR QUEUE USING ARRAY ---")
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
