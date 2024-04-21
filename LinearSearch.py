def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # Return the index where the target is found
    return -1  # Return -1 if the target is not found

# Example usage:
arr = [3, 7, 2, 9, 4]
target = 9
result = linear_search(arr, target)
if result != -1:
    print("Target", target, "found at index", result)
else:
    print("Target", target, "not found in the array.")
