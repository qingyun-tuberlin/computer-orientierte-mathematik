
def selectionSortDivisable(A):

    """
    普通 selection sort 是根据 大小关系（<) 来比较和交换。
    这里的版本不是按照大小排序，
    而是按照整除关系 (Teilbarkeitsrelation) 来交换。
    也就是说：
    当 A[i] 能被 A[j] 整除（即 A[i] % A[j] == 0),
    就把 A[j] 和 A[i] 换位置。
    结果不是一个通常意义上的“排序”（升序或降序），
    而是一个满足 整除关系的部分有序排列。
    """

    # Sort the given list A
    n = len(A)
    for i in range(0, n-1):          # 外层循环：位置 i
        for j in range(i+1, n):      # 内层循环：位置 j
            if A[i] % A[j] == 0:     # 如果 A[i] 可以被 A[j] 整除
                A[i], A[j] = A[j], A[i]   # 就交换 A[i] 和 A[j]

A = [int(x) for x in input().split()]
selectionSortDivisable(A)
print(A)


"""
i = 0, A[i] = 8
j = 1: 8 % 4 == 0 → 交换 → [4, 8, 2]
j = 2: 4 % 2 == 0 → 交换 → [2, 8, 4]
i = 1, A[i] = 8
j = 2: 8 % 4 == 0 → 交换 → [2, 4, 8]

"""