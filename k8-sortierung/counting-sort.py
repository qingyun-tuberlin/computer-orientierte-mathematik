# 参照课件中伪代码的实现
A = [5,4,3,2,1,1,1,6]
n = len(A)
k = max(A)

C = list([0]*(k+1)) 
    
for j in range(0,n):
    C[A[j]] = C[A[j]] + 1
print("C: ", C)

for i in range(0,k):
    C[i+1] = C[i+1] + C[i]
print("C: ", C)

B = list([False]*n)
print("A: ", A)
j = n-1
while j >= 0:
    B[C[A[j]] - 1] = A[j]
    C[A[j]] = C[A[j]] - 1
    j -= 1
print(B)


# C = list([0]*(k+1)). 为什么要 k+1 个格子？<br>
# 因为 Python 的数组/列表是从 0 开始索引的：<br>
# 如果元素的最大值是 k，那么可能的元素是：<br>
# 0,1,2,…,k<br>
# 一共 k+1 个不同的数。<br>
# 所以 C 必须有 k+1 个位置，分别存储：<br>
# C[0]: 值为 0 的元素出现次数<br>
# C[1]: 值为 1 的元素出现次数<br>
# …<br>
# C[k]: 值为 k 的元素出现次数<br>
# 如果只写 [0]*k，那 C 的合法下标是 0 … k-1，就存不下 A 里值等于 k 的情况，<br>
# 会报 IndexError。<br>

# B[C[A[j]] - 1] = A[j] 为什么要 -1 <br>
# 为数组索引是 0-based，而前缀和数组 C 里存的是 1-based 的排名 <br>
# 如果 C[3] = 5，说明值 ≤ 3 的一共有 5 个 <br>
# 那么最后一个 3 在结果数组里应该放在第 5 个位置 <br>
# 件算法写的是： <br>
# B[C[A[j]]] ← A[j] <br>
# C[A[j]] ← C[A[j]] - 1 <br>
# 这里默认的是 数学书上的数组是从 1 开始编号的。 <br>



# 等价表达
# for j in range(0,n):
#     C[A[j]] = C[A[j]] + 1
# print("C: ", C)

# for x in A:
#     C[x] += 1
# A[j] == x


# while j >= 0:
#     B[C[A[j]] - 1] = A[j]
#     C[A[j]] = C[A[j]] - 1
#     j -= 1

# for j in range(n - 1, -1, -1):
#     x = A[j]
#     B[C[x] - 1] = x
#     C[x] -= 1