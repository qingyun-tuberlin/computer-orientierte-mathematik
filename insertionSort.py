def insertionSort(arr):
    
    printArray(arr)
    print("#")
    for i in range(1, len(arr)):
        s = arr[i]
        k = i 

        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        print("#")
        while k > 0 and s < arr[k-1]:
            arr[k] = arr[k-1]
            k -= 1
            printArray(arr)
        arr[k] = s
        printArray(arr)
        
# A utility function to print array of size n
def printArray(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()

arr = [5, 4, 3, 2, 1]
insertionSort(arr)
