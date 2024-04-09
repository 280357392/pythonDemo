# 定义字符串，字符串可以用双引号定义，也可以用单引号定义。支持灵活定义包含引号或撇号的字符串。
name = "ada lovelace"
# name = '"hello"'
# name 变量指向一个已实例化的 str（class） 对象。(class str 定义在 builtins.py 模块中)
# 对象以点的方式调用（标准库）自带的方法。
# 每个不一样的字符串都是不同的对象。id(obj)
# 调用方法后的值只是暂时的，如要改变原来的变量就需要重新赋值。
print(name.title())  # Ada Lovelace
print(name)  # ada lovelace
name = name.title()
# 查看文档，字符串对象中所有方法的使用说明：
# https://docs.python.org/zh-cn/3.8/library/stdtypes.html#string-methods


# 字符串中插入变量
#   使用F 和 大括号
#   f字符串是v3.6引入的
first_name = 'a"d"a'
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
#   v3.6以前应使用 format 方法
full_name2 = "{} {}".format(first_name, last_name)

# 支持制表符和换行符等。
# print自带换行效果。
print("\t 1")
print("2\n ")
