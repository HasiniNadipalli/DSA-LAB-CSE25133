stack = []

# Push operation
def push():
    value = int(input("Enter element: "))
    stack.append(value)
    print("Element pushed.")

# Pop operation
def pop():
    if len(stack) == 0:
        print("Stack is empty.")
    else:
        print("Popped element:", stack.pop())

# Peek operation
def peek():
    if len(stack) == 0:
        print("Stack is empty.")
    else:
        print("Top element:", stack[-1])

# Display operation
def display():
    if len(stack) == 0:
        print("Stack is empty.")
    else:
        print("Stack elements:")
        for i in range(len(stack) - 1, -1, -1):
            print(stack[i])

# Main program
while True:
    print("\n--- STACK USING ARRAY ---")
    print("1. Push")
    print("2. Pop")
    print("3. Peek")
    print("4. Display")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        push()

    elif choice == 2:
        pop()

    elif choice == 3:
        peek()

    elif choice == 4:
        display()

    elif choice == 5:
        print("Program exited.")
        break

    else:
        print("Invalid choice.")
