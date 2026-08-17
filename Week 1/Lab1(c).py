def search(list, key, index):
    if index >= len(list):
        return False

    if list[index] == key:
        return True

    return search(list, key, index + 1)

employees = [101, 102, 103, 104, 105]

key = int(input("Enter Employee ID to search: "))

if search(employees, key, 0):
    print("Employee ID Found")
else:
    print("Employee ID Not Found")
