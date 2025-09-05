
# 方法一：动态规划 O(n²)
# 复杂度：O(n²)，适合 n ≤ 2000 左右。
def LIS_quadratic(arr):
    n = len(arr)
    dp = [1] * n
    for i in range(n):
        for j in range(i):
            if arr[j] < arr[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)

#方法二：贪心 + 二分 O(nlogn)
# 复杂度：O(n log n)，可以处理 n = 10^5 或更多。
import bisect

def LIS_logN(arr):
    tails = []
    for x in arr:
        pos = bisect.bisect_left(tails, x)  # 找到插入位置
        if pos == len(tails):
            tails.append(x)
        else:
            tails[pos] = x
    return len(tails)
