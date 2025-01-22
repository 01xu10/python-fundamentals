# -*- coding:utf-8 -*-
# ---------^-^----------
# @Time : 2025/1/20 17:40
# @Author : chenxx
# @Email : 1150772265@qq.com
# @File : int_type.py
# ----------------------


"""整形"""
# 定义
count = 2
index = -2
total = 100
z = 0

# 运算
s = count + index  # 0
t = count * index  # -4
u = total / count  # 50

count = 2
total = 7
# 进阶运算
# 两个整数相除并向下取整
result1 = 7 // 3
print(result1)  # 输出 2，因为 7 除以 3 商为 2 余 1，整除运算符只取商的整数部分

# 整数的取模运算
remainder1 = 7 % 3
print(remainder1)  # 输出 1，因为 7 除以 3 商为 2 余 1

# 平方根运算
square_root = 16 ** 0.5
print(square_root)  # 输出 4.0，因为 16 的平方根是 4


# 作为列表的索引
my_list = ['apple', 'banana', 'cherry']
print(my_list[count])  # 'cherry'

# 核心函数
# bin() 将整数转换为二进制
num = 10
binary_num = bin(num)
print(f"The binary representation of {num} is {binary_num}")

# oct() 将整数转换为八进制
octal_num = oct(num)
print(f"The octal representation of {num} is {octal_num}")

# hex() 将整数转换为十六进制
hex_num = hex(num)
print(f"The hexadecimal representation of {num} is {hex_num}")

# abs() 求绝对值
negative_num = -15
absolute_num = abs(negative_num)
print(f"The absolute value of {negative_num} is {absolute_num}")

# divmod() 求商和余数
quotient, remainder = divmod(20, 3)
print(f"When dividing 20 by 3, the quotient is {quotient} and the remainder is {remainder}")
# 20 / 3 = 6...2  quotient = 6, remainder = 2
# 20 / 3 = 6.666666666666667  quotient = 6

# pow() 求幂
power = pow(2, 3)
print(f"2 raised to the power of 3 is {power}")  # 8

# round() 四舍五入
rounded_num = round(3.14159, 2)
print(f"The rounded value of 3.14159 to 2 decimal places is {rounded_num}")  # 3.14

# isinstance() 判断是否为某个类型
print(isinstance(10, int))  # True
print(isinstance(10.5, int))  # False

# sqrt() 求平方根
import math

sqrt_num = math.sqrt(16)
print(f"The square root of 16 is {sqrt_num}")  # 4.0

# ** 指数运算
sqrt_num = 16 ** 0.5
print(f"The square root of 16 is {sqrt_num}")  # 4.0

a = 2 ** 3
print(a)  # 8  2 * 2 * 2= 8


"""浮点数"""
# 定义


"""复数"""
