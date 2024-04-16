bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)
print(bicycles[0])
print(bicycles[-2])  # redline 倒数第二个
# print(bicycles[99])  # 报错 IndexError: list index out of range

# 修改、添加、删除
a = [1, 2, 3]
b = a
a[0] = 100  # 修改，a和b指向同一个id，因此当修改a的元素时也会影响b。
a.append(4)  # 末尾添加元素。
a.insert(0, 99)  # 开始的位置插入元素。
del a[0]  # 删除第一个元素。
del a[1:3]  # 删除第二个元素到第三个元素。
# del a[:]  # 清空list
# del a[99]  # 报错 IndexError: list assignment index out of range
result = a.pop(1)  # 根据索引（未传参时默认删除最后一个）删除元素，并返回被删除的元素。

# 删除后不再使用元素时 使用del
# 删除后继续使用元素时 使用pop

names = ['Alice', 'Bob', 'Bob', 'Charlie']
# names.remove('Bob') # 根据值来删除，最多只会删除一个。可以使用循环来删除所有的值。
while True:
    if 'Bob' not in names:
        break
    names.remove('Bob')

# 排序（永久）
my_list = ['zhangsan', 'lisi', 'bob', 'alex']
my_list.sort()

# 翻转 (永久，再次翻转可恢复)
cars = ['bmw', 'audi', 'toyota']
# cars.reverse()

# 长度len
print(cars[len(cars) - 1])

