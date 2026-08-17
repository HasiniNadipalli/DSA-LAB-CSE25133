# Selection Sort

def selection_sort(arr):
    n = len(arr)

    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

# Taking input

n = int(input("Enter number of elements: "))
arr = []
print("Enter elements: ")
for i in range(n):
    arr.append(int(input()))

# Sorting the array

selection_sort(arr)

# Displaying sorted array

print("Sorted array: ")
for element in arr:
    print(element, end=" ")
