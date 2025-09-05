# Task c (3 points)
# Es sei eine Liste L von n ganzen Zahlen gegeben. Schreiben Sie eine Python-Funktion
# duplicates (L), die in Laufzeit O(nlogn) eine geordnete Liste der Elemente aus L
# zurückgibt, welche in L mindestens doppelt vorkommen.
# 输入：一个整数列表 L，长度为 n
# 返回一个有序列表（升序），其中包含那些在 L 中至少出现两次的元素
# 时间复杂度：O(n log n)

def merge_sort(a):
    """归并排序：稳定，最坏 O(n log n)，额外空间 O(n), merge sort is not in-place"""
    n = len(a)
    if n <= 1:
        return a[:]  # 返回副本，避免原地修改
    mid = n // 2
    left = merge_sort(a[:mid])
    right = merge_sort(a[mid:])
    return _merge(left, right)

def _merge(left, right):
    i = j = 0
    res = []
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:      # 稳定性：<= 保持相等时左边先
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1
    # 拼接剩余部分
    if i < len(left):
        res.extend(left[i:])
    if j < len(right):
        res.extend(right[j:])
    return res

def duplicates(L):
    """
    返回升序列表，包含在 L 中至少出现两次的元素（不重复列出）。
    总复杂度：归并排序 O(n log n) + 一次线性扫描 O(n)。
    """
    if not L:
        return []
    S = merge_sort(L)   # 手写排序，O(n log n)
    out = []
    # 相邻去重扫描
    for i in range(1, len(S)):
        if S[i] == S[i-1]:
            if not out or out[-1] != S[i]:
                out.append(S[i])
    return out


print(duplicates([4, 2, 3, 2, 5, 3]))
print(duplicates([1, 2, 3, 4]))         # []
print(duplicates([5, 5, 5, 5]))         # [5]
print(duplicates([]))