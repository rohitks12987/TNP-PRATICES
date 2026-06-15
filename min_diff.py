def min_diff(arr1, arr2):
    arr1.sort()
    arr2.sort()
    i = j = 0
    diff = float('inf')
    while i < len(arr1) and j < len(arr2):
        diff = min(diff, abs(arr1[i] - arr2[j]))
        if arr1[i] < arr2[j]:
            i += 1
        else:
            j += 1
    return diff
arr1 = list(map(int, input("Enter first array: ").split()))
arr2 = list(map(int, input("Enter second array: ").split()))

print("Minimum difference:", min_diff(arr1, arr2))
