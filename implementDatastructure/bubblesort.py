class Sort:
    def bubble_sort(self, arr):
        n = len(arr)
        # Traverse through all array elements
        for i in range(n):
            # Last i elements are already in place
            # Optimization: If no two elements were swapped by inner loop, then break
            swapped = False
            for j in range(0, n - i - 1):
                # Traverse the array from 0 to n-i-1
                # Swap if the element found is greater than the next element
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    swapped = True
            # If no two elements were swapped in inner loop, then break
            if not swapped:
                break
        return arr

# Example usage:
s=Sort()
my_list = [64, 34, 25, 12, 22, 11, 90]
sorted_list = s.bubble_sort(my_list)
print(f"Sorted array: {sorted_list}")