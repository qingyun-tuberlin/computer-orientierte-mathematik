# 在 Python 中，可迭代对象 (iterable) 指的是：
# 可以被逐个遍历的对象。
# 换句话说：如果一个对象能用在 for ... in ... 循环 里，那它就是可迭代对象。

# 一个对象是可迭代的，当它实现了：
# __iter__() 方法（返回一个迭代器），或者
# __getitem__() 方法（从索引 0 开始，支持逐个取值）。

# 常见的可迭代对象
# 字符串："hello" → 可以一个一个字符地取。
# 列表：[1,2,3]
# 元组：(1,2,3)
# 集合：{1,2,3}
# 字典：{"a":1,"b":2}（遍历时默认遍历 key）
# range 对象：range(5)

# 字符串
for c in "abc":
    print(c)

# 列表
for x in [1, 2, 3]:
    print(x)

# 字典
for k in {"a": 1, "b": 2}:
    print(k)


# 可迭代 vs 迭代器
# 可迭代对象 (iterable)：能产生迭代器的“容器”。
# 迭代器 (iterator)：实际执行逐个取值的对象。
# 迭代器实现了 __next__() 方法。

s = "abc"
it = iter(s)   # 通过 iter() 得到迭代器
print(next(it))  # 'a'
print(next(it))  # 'b'
print(next(it))  # 'c'
