def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i   # return index if found
    return -1          # return -1 if not found

# Example usage
numbers = [10, 25, 30, 45, 50]
search_for = 30
result = linear_search(numbers, search_for)

if result != -1:
    print(f"Element found at index {result}")
else:
    print("Element not found")
