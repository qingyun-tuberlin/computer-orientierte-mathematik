

def insertionSort(A):
    n = len(A)
    for i in range(1, n):       # 从第二个元素开始 (第0个元素默认有序)
        s = A[i]                # 当前要插入的数
        k = i                   # 从位置 i 开始往前比较

        while k > 0 and s < A[k-1]:   # 如果前一个元素比 s 大，就把前一个元素往后挪
            A[k] = A[k-1]
            k -= 1
        A[k] = s                # 找到合适位置，把 s 放进去

A = input().split()
insertionSort(A)
print(A)



