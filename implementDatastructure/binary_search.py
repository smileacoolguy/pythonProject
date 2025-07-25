class search:
    def binary_search(arr, target_value):
        low = 0
        high = len(arr) - 1

        while low <= high:
            mid = (low + high) // 2
            if arr[mid] == target_value:
                return mid  # Target found, return its index
            elif arr[mid] < target_value:
                low = mid + 1  # Target is in the right half
            else:
                high = mid - 1  # Target is in the left half
        return -1  # Target not found

# Example Usage:
sorted_list = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
target = 11
result = search.binary_search(sorted_list, target)

if result != -1:
    print(f"Element {target} found at index {result}")
else:
    print(f"Element {target} not found in the list")
