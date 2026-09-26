class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    # 1. Create linked list
    def create(self):
        n = int(input("Enter number of nodes: "))

        for i in range(n):
            data = int(input(f"Enter data for node {i + 1}: "))
            new_node = Node(data)

            if self.head is None:
                self.head = new_node
            else:
                temp = self.head
                while temp.next:
                    temp = temp.next
                temp.next = new_node

        print("Linked list created successfully.")

    # 2. Insert at beginning
    def insert_beginning(self):
        data = int(input("Enter data: "))
        new_node = Node(data)

        new_node.next = self.head
        self.head = new_node

        print("Node inserted at beginning.")

    # 3. Insert at end
    def insert_end(self):
        data = int(input("Enter data: "))
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node

        print("Node inserted at end.")

    # 4. Insert at specific index
    def insert_index(self):
        index = int(input("Enter index: "))
        data = int(input("Enter data: "))
        new_node = Node(data)

        if index == 0:
            new_node.next = self.head
            self.head = new_node
            print("Node inserted.")
            return

        temp = self.head

        for i in range(index - 1):
            if temp is None:
                print("Invalid index.")
                return
            temp = temp.next

        if temp is None:
            print("Invalid index.")
            return

        new_node.next = temp.next
        temp.next = new_node

        print("Node inserted.")

    # 5. Delete by value
    def delete_value(self):
        value = int(input("Enter value to delete: "))

        if self.head is None:
            print("List is empty.")
            return

        if self.head.data == value:
            self.head = self.head.next
            print("Node deleted.")
            return

        temp = self.head

        while temp.next and temp.next.data != value:
            temp = temp.next

        if temp.next is None:
            print("Value not found.")
        else:
            temp.next = temp.next.next
            print("Node deleted.")

    # 6. Delete first node
    def delete_first(self):
        if self.head is None:
            print("List is empty.")
        else:
            self.head = self.head.next
            print("First node deleted.")

    # 7. Delete last node
    def delete_last(self):
        if self.head is None:
            print("List is empty.")
            return

        if self.head.next is None:
            self.head = None
            print("Last node deleted.")
            return

        temp = self.head

        while temp.next.next:
            temp = temp.next

        temp.next = None
        print("Last node deleted.")

    # 8. Count nodes
    def count(self):
        count = 0
        temp = self.head

        while temp:
            count += 1
            temp = temp.next

        print("Number of nodes:", count)

    # 9. Display / Traverse
    def display(self):
        if self.head is None:
            print("List is empty.")
            return

        temp = self.head

        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next

        print("None")


# Main program
sll = SinglyLinkedList()

while True:
    print("\n--- SINGLY LINKED LIST ---")
    print("1. Create linked list")
    print("2. Insert at beginning")
    print("3. Insert at end")
    print("4. Insert at specific index")
    print("5. Delete by value")
    print("6. Delete first node")
    print("7. Delete last node")
    print("8. Count number of nodes")
    print("9. Display / Traverse")
    print("10. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        sll.create()

    elif choice == 2:
        sll.insert_beginning()

    elif choice == 3:
        sll.insert_end()

    elif choice == 4:
        sll.insert_index()

    elif choice == 5:
        sll.delete_value()

    elif choice == 6:
        sll.delete_first()

    elif choice == 7:
        sll.delete_last()

    elif choice == 8:
        sll.count()

    elif choice == 9:
        sll.display()

    elif choice == 10:
        print("Program exited.")
        break

    else:
        print("Invalid choice.")
