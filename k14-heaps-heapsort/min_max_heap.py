def left(i): return 2*i

def right(i): return 2*i +1

def parent(i): return i//2

def max_heapify(A,i,n=None):
    # print("A is: ", A, "i is: ", i)
    l,r,largest = left(i), right(i), i 
    # suppose the first elemet of A is None, index starts at 1
    if n==None:
        n = len(A) - 1

    if l <= n and A[l] > A[largest]:
        largest = l
    if r <= n and A[r] > A[largest]:
        largest = r

    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        max_heapify(A,largest,n)
        
def build_max_heap(A,):
    n = len(A)-1
    for i in range(n //2,0,-1):
        # print("in build max heap, i is:", i)
        max_heapify(A,i)


def heap_sort(A):
    build_max_heap(A)
    print(A)
    n = len(A)-1

    while n > 0:
        A[1], A[n] = A[n], A[1]
        n -= 1
        # 把堆的大小缩小 n -= 1（因为最后的元素已经排好序，不再属于堆）。
        # 这时堆的元素只包含 A[1..n]，后面的 A[n+1..end] 已经是有序区，不能参与堆化
        max_heapify(A,1,n)


def min_heapify(A,i,n=None):
    l,r,smallest = left(i), right(i), i 
    if n==None:
        n = len(A) - 1
    if l <= n and A[l] < A[smallest]:
        smallest = l
    if r <= n and A[r] < A[smallest]:
        smallest = r
    if smallest != i:
        A[i], A[smallest] = A[smallest], A[i]
        min_heapify(A,smallest,n)


def build_min_heap(A,):
    n = len(A)-1
    for i in range(n //2,0,-1):
        min_heapify(A,i)

def heap_sort_with_min_heap(A):
    build_min_heap(A)
    n = len(A)-1
    while n > 0:
        A[1], A[n] = A[n], A[1]
        n -= 1
        min_heapify(A,1)

A = [None, 3, 4, 10, 14, 7, 9, 16, 2, 8, 1]
build_min_heap(A)
print("min heap: ", A,"\n")
A = [None, 3, 4, 10, 14, 7, 9, 16, 2, 8, 1]
build_max_heap(A)
print("max heap: ", A,"\n")

A = [None, 3, 4, 10, 14, 7, 9, 16, 2, 8, 1]
heap_sort_with_min_heap(A)
print(A,"\n")
    
