
def selectionSort(A):
    
    """
    这是 选择排序(Selection Sort)的一种实现方式。
    外层循环 i:表示当前要放置“最小值”的位置。
    内层循环 j:从 i+1 开始,依次和 A[i] 比较,找到比它更小的值就交换。
    这样,每一轮外层循环结束后,A[i] 就是从 i..n-1 范围里最小的数。
    最终数组会变成升序排列。

    This algorithm is in-place.
    It only rearranges the array inside A using swaps, 
    and needs no extra data structure (only O(1) additional space).

    This algorithm is not stable.
    Let A = [(2, 'a'), (2, 'b'), (1, 'c')] where I mark duplicates with labels.
    At the first iteration (i=0, j=2): 1 < 2 → swap (2, 'a') and (1, 'c').
    New order: [(1, 'c'), (2, 'b'), (2, 'a')].
    Notice: originally (2,'a') came before (2,'b'). 
    After sorting, (2,'b') comes before (2,'a'). 
    Relative order of equal 2s got reversed → not stable.

    """
    
    n = len(A)   # 计算数组长度
    for i in range(0, n-1):   # 外层循环:从第0个到倒数第2个元素
        for j in range(i+1, n):   # 内层循环:从 i 之后的元素开始比较
            if A[j] < A[i]:   # 如果发现比 A[i] 更小的元素
                A[i], A[j] = A[j], A[i]   # 交换 A[i] 和 A[j]



A = input().split()  # example: 3 1 2 
selectionSort(A)
print(A)


"""
输入后 A = ['9', '3', '7', '1']（注意：是字符串！）
i = 0
j = 1: '3' < '9' → 交换 → ['3','9','7','1']
j = 2: '7' < '3'? 否
j = 3: '1' < '3' → 交换 → ['1','9','7','3']
→ 位置0已确定最小值 '1'
i = 1
j = 2: '7' < '9' → 交换 → ['1','7','9','3']
j = 3: '3' < '7' → 交换 → ['1','3','9','7']
i = 2
j = 3: '7' < '9' → 交换 → ['1','3','7','9']
结果：['1','3','7','9']

"""