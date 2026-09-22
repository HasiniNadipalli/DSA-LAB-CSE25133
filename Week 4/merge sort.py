def merge_sort(arr):
    # Base condition
    if len(arr) <= 1:
        return arr

    # Divide the array
    mid = len(arr) // 2

    left = arr[:mid]
    right = arr[mid:]

    # Recursive calls
    left = merge_sort(left)
    right = merge_sort(right)

    # Merge the two sorted halves
    i = j = k = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    # Copy remaining elements of left array
    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1

    # Copy remaining elements of right array
    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1

    return arr


# Main program
n = int(input("Enter number of elements: "))

arr = []

print("Enter elements:")
for i in range(n):
    arr.append(int(input()))

merge_sort(arr)

print("Sorted array:")
for element in arr:
    print(element, end=" ")
