stack = []
while True:
    print("\n--- STACK USING ARRAY ---")
    print("1. Push")
    print("2. Pop")
    print("3. Peek")
    print("4. Display")
    print("5. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        value = int(input("Enter element: "))
        stack.append(value)
        print("Element pushed")
    elif choice == 2:
        if len(stack) == 0:
            print("Stack is empty")
        else:
            print("Popped element:", stack.pop())
    elif choice == 3:
        if len(stack) == 0:
            print("Stack is empty")
        else:
            print("Top element:", stack[-1])
    elif choice == 4:
        if len(stack) == 0:
            print("Stack is empty")
        else:
            print("Stack:")
            for i in range(len(stack) - 1, -1, -1):
                print(stack[i])
    elif choice == 5:
        print("Program ended")
        break
    else:
        print("Invalid choice")
