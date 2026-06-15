arr = list(map(int, input("Enter numbers: ").split()))
sorted_arr = sorted(arr, key=lambda x: x)
print("Sorted array:", sorted_arr)
