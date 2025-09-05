
# task c, 3 points
# Es sei eine positive ganze Zahl n gegeben. Schreiben Sie eine Python-Funktion
# ascendingsequence (n), die in Laufzeit O(logn) die Länge der längsten aufsteigen-
# den konsekutiven Teilfolge von Ziffern von n zurückgibt.

# 方法一：转成字符串扫描（简单清晰）
def ascendingsequence(n: int) -> int:
    s = str(n)
    best = cur = 1
    for i in range(1, len(s)):
        if s[i] > s[i-1]:   # 严格上升
            cur += 1
        else:
            cur = 1
        if cur > best:
            best = cur
    return best


# 方法二：纯算术做法（不转字符串）
def ascendingsequence_v2(n: int) -> int:
    # 至少一位
    best = cur = 1
    prev = n % 10      # 取最低位
    n //= 10

    while n > 0:
        d = n % 10     # 下一位（更高位）
        # 从左到右看，如果 d < prev，则 d(左) < prev(右) —— 左到右严格递增
        if d < prev:
            cur += 1
        else:
            cur = 1
        if cur > best:
            best = cur
        prev = d
        n //= 10

    return best


print(ascendingsequence(12345))
print(ascendingsequence(12315))