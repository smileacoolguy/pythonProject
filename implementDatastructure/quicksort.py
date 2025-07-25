def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]  # Choosing the middle element as pivot
        less = [x for x in arr if x < pivot]
        equal = [x for x in arr if x == pivot]
        greater = [x for x in arr if x > pivot]
        return quicksort(less) + equal + quicksort(greater)

# Example usage:
my_list = [5, 2, 8, 10, 3, 0, 4]
sorted_list = quicksort(my_list)
print(sorted_list)



###################
import sys

if __name__ == "__main__":
    print(f"Number of arguments: {len(sys.argv)}")
    print(f"Argument list: {sys.argv}")

    if len(sys.argv) > 1:
        print(f"First argument (excluding script name): {sys.argv[1]}")