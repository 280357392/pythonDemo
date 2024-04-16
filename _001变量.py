# 定义变量 message，message 指向一个内存地址0x001，0x001内存中存储了 "hello python world!" 字符。
message = "hello python world!"
print(message)
# 修改变量
message = "hello python world! 新的值"

# 同时定义变量
x, y, z = 1, 2, 3
print(x, y, z)

if __name__ == '__main__':  # 代码从上往下运行
    # 使用变量 message
    print(message)
    # 使用未定义的变量将报错：NameError: name 'message2' is not defined
    # print(message2)
