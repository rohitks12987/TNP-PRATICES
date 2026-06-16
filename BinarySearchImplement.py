def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2   # middle index
        
        if arr[mid] == target:
            return mid              # found target
        elif arr[mid] < target:
            left = mid + 1          # search right half
        else:
            right = mid - 1         # search left half
    
    return -1                       # not found

# Example usage
numbers = [10, 20, 30, 40, 50, 60]
search_for = 40

result = binary_search(numbers, search_for)

if result != -1:
    print(f"Element found at index {result}")
else:
    print("Element not found")