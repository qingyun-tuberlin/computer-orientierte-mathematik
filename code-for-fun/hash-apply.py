#在一个数字列表中，找出两个数字，使它们的和等于一个特定的目标值。

# Intuitive & Brute-Force Approach
# Time Complexity O(n^2)
def two_sum_brute_force(nums, target):
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == target:
                return [i, j]
    return None


# Abstract, Mathematical & Analytical Approach
# Time Complexity O(n)
def two_sum_hash_map(nums, target):
    """
        算法体现：
        初始化一个空的哈希表（字典）。
        遍历列表中的每个数字 num 及其索引 i。
        对于每个 num, 计算其补数 complement = target - num。
        在哈希表中查找这个补数是否已经存在。
        如果存在，说明我们找到了答案：[当前补数的索引, 当前索引 i]。
        如果不存在，则将当前数字 num 和它的索引 i 存入哈希表，以备后续查找。
    """
    hash_map = {} # 创建一个空字典，用于存储“数字:索引”
    for i, num in enumerate(nums):
        complement = target - num
        if complement in hash_map: # 查找补数是否在哈希表中（O(1)操作）
            return [hash_map[complement], i]
        hash_map[num] = i # 将当前数字存入哈希表
    return None

print(two_sum_hash_map([1,2,3,4],5))
