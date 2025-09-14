
def mergeSort(A):
    if len(A) <= 1:           # 如果数组只有一个元素或为空
        return(A)             # 已经有序，直接返回
    else:
        return(merge(         # 否则：
            mergeSort(A[:len(A)//2]),    # 递归排序左半部分
            mergeSort(A[len(A)//2:])     # 递归排序右半部分
        ))

def merge(left, right):
    merged = []
    while left and right:                 # 当左右数组都非空时
        if left[0] < right[0]:            # 比较两边的第一个元素
            merged.append(left[0])        # 取较小的放进 merged
            left = left[1:]               # 删除左边第一个元素
        else:
            merged.append(right[0])       # 否则取右边的
            right = right[1:]
    merged.extend(left + right)           # 把剩下的直接接到结果后面
    return merged

A = input().split() # Beispiel: 4 3 2 1
A = [int(x) for x in A]
print(mergeSort(A))



"""

拆分 [4,3,2,1] → [4,3] + [2,1]
[4,3] → [4] + [3] → merge → [3,4]
[2,1] → [2] + [1] → merge → [1,2]
merge [3,4] 和 [1,2] → [1,2,3,4]

"""