# Creating a bubble sort function
def bubble_sort(arr):
    # Outer loop for traverse the entire list
    for i in range(0, len(arr) - 1):
        for j in range(len(arr) - 1):
            if (arr[j] > arr[j + 1]):
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp
    print (arr)


arr = []
n = int(input("Enter number of elements : "))

for i in range(0, n):
    ele = int(input("Enter element : "))
    arr.append(ele)
print(arr)
bubble_sort(arr)