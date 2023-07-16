
# Binary search function
def binary_search(arr,target):
    left_bound = 0
    right_bound = len(arr)
    while left_bound <= right_bound:
        mid= (left_bound + right_bound)//2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left_bound = mid + 1
        else:
            right_bound = mid - 1
    # if target not in arr:
    return -1

# Example usage:
my_list = [1, 3, 5, 0,7, 9, 11, 13, 15, 17,0,56]
target_element = 7
result=binary_search(my_list,target_element)

if result != -1:
    print("Element is present at index", str(result))
else:
    print("Element is not present in array")