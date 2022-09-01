def binary_search(data, element, low, high):
    # data is sorted in ascending order

    if low > high:  # if (low>high):an empty list state and it indicates that element is not present in the list named data

        return False
    else:  # low<=high

        mid = (low + high) // 2
        if element == data[mid]:
            return True
        elif element < data[mid]:
            # search in the first half of the list, data
            return binary_search(data, element, low, mid - 1)
        else:
            return binary_search(data, element, mid + 1, high)

# Test array
arr = [2, 3, 4, 10, 40]
x = 10

# Function call
result = binary_search(arr, x, 0, len(arr)-1)

if result != -1:
    print(str(result))
else:
    print("Element is not present in array")