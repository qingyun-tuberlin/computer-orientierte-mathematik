
# GPT 给的实现
from typing import List

def counting_sort_by_digit(A: List[int], base: int, exp: int) -> None:
    """
    对 A 按当前位进行稳定的计数排序（就地写回）。
    当前位 = (A[i] // exp) % base
    exp = 1 表示个位，10 表示十位，依此类推。
    """
    n = len(A)
    C = [0] * base            # 计数数组：0..base-1
    B = [0] * n               # 临时输出，保证稳定性

    # 统计每个“当前位值”的出现次数
    for x in A:
        digit = (x // exp) % base
        C[digit] += 1

    # 前缀和 → C[v] 变为 <= v 的元素个数
    # C[v] = “所有 digit ≤ v 的元素总数”
    # 这样我们就知道每个 digit 的最终位置范围，便于下一步稳定回填。
    for v in range(1, base):
        C[v] += C[v - 1]

    # 逆序回填，保证稳定
    for i in range(n - 1, -1, -1):
        digit = (A[i] // exp) % base
        C[digit] -= 1           # 找到下一个可用位置。
        B[C[digit]] = A[i]      # 把元素放到输出数组里。

    # 写回 A
    A[:] = B


def radix_sort(A: List[int], base: int = 10) -> List[int]:
    """
    LSD Radix Sort（非比较排序），默认十进制。
    只处理非负整数；若有负数，见下面的扩展函数 radix_sort_with_negatives。
    返回排序后的同一列表（就地排序）。
    复杂度：O(d * (n + base))，通常记作 O(n * d)；空间 O(n + base)。
    """
    if not A:
        return A
    if min(A) < 0:
        raise ValueError("radix_sort 仅处理非负整数；请使用 radix_sort_with_negatives。")

    m = max(A)
    exp = 1
    while m // exp > 0:
        counting_sort_by_digit(A, base, exp)
        exp *= base
    return A


# —— 可选：支持负数的版本 ——
def radix_sort_with_negatives(A: List[int], base: int = 10) -> List[int]:
    """
    拆分负数与非负数：
      - 对非负数组直接做 radix_sort；
      - 对负数取绝对值做 radix_sort，最后倒序并加回负号（因为 -9 < -1）。
    """
    neg = [-x for x in A if x < 0]
    pos = [x for x in A if x >= 0]

    if neg:
        radix_sort(neg, base)
        neg = [-x for x in reversed(neg)]   # 还原为递增：如 [-9,-3,-1]
    if pos:
        radix_sort(pos, base)
    A[:] = neg + pos
    return A

A = [329, 457, 657, 839, 436, 720, 355]
print(radix_sort(A))  # [329, 355, 436, 457, 657, 720, 839]

B = [3, 0, 12, 5, 1, 100, 9]
print(radix_sort(B))  # [0, 1, 3, 5, 9, 12, 100]

C = [10, -3, 7, -20, 0, 5]
print(radix_sort_with_negatives(C))  # [-20, -3, 0, 5, 7, 10]