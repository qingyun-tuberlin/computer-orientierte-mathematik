# task b, 3 points
# Es sei eine 13-stellige positive ganze Zahl n gegeben sowie eine 3-stellige positive
# ganze Zahl k. Schreiben Sie eine Python-Funktion partialsequence(n,k), die True
# zurückgibt, falls die Folge der Ziffern von n die Folge der Ziffern von k als konseku-
# tive Teilfolge enthält. Es dürfen dabei ausschließlich arithmetische Operationen und
# Vergleiche verwendet werden. Insbesondere dürfen weder n noch k in einen String
# oder eine Liste umgewandelt werden.

def partialsequence(n: int, k: int) -> bool:
    # 题设：k 为 3 位正整数
    # “滑动窗口”思想， 就是把“字符串扫描”换成“算术扫描”。
    if k < 100 or k > 999:
        raise ValueError("k must be a 3-digit positive integer (100..999).")
    
    # 当 n 至少还有 3 位时，才能形成一个 3 位窗口
    while n >= 100:
        if n % 1000 == k:   # 末尾三位是否等于 k
            return True
        n //= 10            # 去掉 n 的最后一位，窗口左移一位
    return False


print(partialsequence(1234567890123, 789))  # True
print(partialsequence(1112223334445, 233))  # True
print(partialsequence(7008009001002, 801))  # False
print(partialsequence(100400700, 400))      # True
