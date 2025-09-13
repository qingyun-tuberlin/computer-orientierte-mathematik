def left(i): return 2*i

def right(i): return 2*i +1

def parent(i): return i//2

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

def heap_sort(A):
    build_min_heap(A)
    n = len(A)-1
    while n > 0:
        A[1], A[n] = A[n], A[1]
        n -= 1
        min_heapify(A,1)


