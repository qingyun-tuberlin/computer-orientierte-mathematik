import math 
def bucketSort(A):
    n = len(A)
    # B = [0] * n
    # for i in range(0,n):
    #     B[i] = []
    
    B = [[] for _ in range(n)] 
    
    for i in range(0,n):
        index = int(n * A[i])
        if index == n:
            index -=1
        B[index].append(A[i])

    print(B)
    for i in range(0,n):
        B[i] = insertionSort(B[i])
    print(B)

    result = []
    for bucket in B:
        result.extend(bucket)

    return result   

def insertionSort(A):

    n = len(A)
    for i in range(0,n):
        sk = A[i]
        j = i
        while j > 0 and sk < A[j-1]:
            A[j]= A[j-1]
            j -= 1
        A[j] = sk
    return A

A = [0.78, 0.17, 0.39, 0.26, 0.72, 0.94, 0.21, 0.12, 0.23, 0.68]
print(bucketSort(A))