def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0

    while low <= high:

        mid = (high + low) // 2

        # Check if x is present at mid
        if arr[mid] < x:
            low = mid + 1

        # If x is greater, ignore left half
        elif arr[mid] > x:
            high = mid - 1

        # If x is smaller, ignore right half
        elif arr[mid] == x:
            return True

            # If we reach here, then the element was not present
    return -1


arr = []
n = int(input("Enter number of elements : "))

for i in range(0, n):
    ele = int(input("Enter element(ascending order) : "))
    arr.append(ele)

print(arr)

x = int(input("Enter element to be searched : "))

# Function call
res = binary_search(arr, x)
if res == -1:
    print("not found")
else:
    print("found")