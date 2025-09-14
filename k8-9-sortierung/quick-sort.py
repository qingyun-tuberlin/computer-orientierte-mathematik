
def quickSort(A):
    if len(A) <= 1:          # 基本情况：长度 ≤ 1，直接返回
        return(A)
    else:
        x = A[0]             # 选择第一个元素作为枢轴
        B = quickSort([s for s in A[1:] if s <= x])  # 小于等于 x 的部分
        C = quickSort([s for s in A[1:] if not s <= x]) # 大于 x 的部分
        return(B + [x] + C)  # 拼接结果

A = input().split()
print(quickSort(A))
