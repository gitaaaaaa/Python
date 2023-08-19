########################
######## string ########
########################
# hi = "hello there"
# name = "gita"
# greet = hi + name
# print(greet)
# greeting = hi + " " + name
# print(greeting)
# ana = hi + (" " + name)*3
# print(ana)



########################
######## output ########
########################
# x = 1
# print(x)
# x_str = str(x)
# print("my fav num is", x, ".", "x =", x)
# print("my fav num is " + x_str + ". " + "x = " + x_str)
# print("my fav num is" + x_str + "." + "x=" + x_str)


#######################
######## input ########
#######################
# text = input("Type anything ...")
# print(5*text)
# num = int(input("Type a number... "))
# print(5*num)

#######################
###### while loop #####
#######################
# tip = input("You are in the Lost Forest. \n************\n************\n    😀\n************\n************\nGo left or right?")
# n = 0 
# while tip == "right" or tip == "Right":
#     if n >= 2:
#       print('😟')
#     tip = input("You're in the Lost Forest. Go left or right? ")
#     n = n + 1
# print("You got out of the Lost Forest!")

#######################
# shortcut with for loop
#######################
# n = 0
# for n in range(5):
#     print(n)

# x=4
# for i in range(0, x):
#   print(i)

#######################
# range(start,stop,step)
#######################
# mysum = 0
# for i in range(7, 10):
#     print(i)
#     mysum += i
# print(mysum) #7, 8, 9

# mysum = 0
# for i in range(5, 11, 2):
#  mysum += i
# print(mysum) # 5, 7, 9

# 编写一个程序，检查3个变量x、y和z，输出其中最大的奇数。如果其中没有奇数， 就输出一个消息进行说明。
# x = int(input('请输入x:'))
# y = int(input('请输入y:'))
# z = int(input('请输入z:'))

# if x > y: 
#     x, y = y, x
# if y > z:
#     y, z = z, y
# print(x, y, z)

# if z%2 == 1:
#     print('z',z)
# elif y%2 ==1:
#     print('y',y)
# elif x%2 == 1:
#     print('x:',x)
# else:
#     print('三个数中没有奇数')


# 2.4 将以下代码中的注释替换为while循环语句。

# numXs = int(input('How many times should I print the letter X? '))
# toPrint = ''
# #concatenate X to toPrint numXs times
# while numXs == 2:
#     toPrint = 'x'
#     break
# print(toPrint)


# 2.4 编写一个程序，要求用户输入10个整数，然后输出其中最大的奇数。如果用户没
# 有输入奇数，则输出一个消息进行说明。
# x = int(input('请输入一个整数: '))
# for i in range(x + 10, x, -1):
#     print(i)
#     if i%2 == 1: 
#         print('最大的奇数', i)
#         break;
    
    # 初始化变量，用于存储最大的奇数和记录是否存在奇数
max_odd = None
has_odd = False

# 循环输入 10 个整数
for _ in range(10):
    num = int(input("请输入一个整数: "))
    
    # 判断输入的数是否为奇数
    if num % 2 == 1:
        # 如果当前数为奇数且之前没有记录奇数，或者当前数大于已记录的最大奇数
        if not has_odd or (has_odd and num > max_odd):
            max_odd = num
            has_odd = True

# 输出结果
if has_odd:
    print("输入的最大奇数是:", max_odd)
else:
    print("没有输入奇数.")









# 如果在循环中改变x的值，能否影响迭代次数?答案是“不能”
# x=4
# for i in range(0, x):
#   print(i) 
#   x=5

# ####### 注意
# 外层循环中的range函数只被求值一次，而内层循环中的range函数则在每次执行内层 for语句时都被求值
# x=4
# for j in range(x):
#   print('---', x)
#   for i in range(x):
#     print(i)
#     x=2

# ####### 注意
#寻找完全立方数的立方根
# x = int(input('Enter an integer: ')) 
# for ans in range(0, abs(x)+1):
#   if ans**3 >= abs(x):
#      break
# if ans**3 != abs(x):
#   print(x, 'is not a perfect cube')
# else:
#   if x < 0:
#     ans = -ans
#     print('Cube root of', x,'is', ans)



# total = 0
# for c in '12345678':
#     total = total + int(c)
# print(total)
  

# 实际练习:假设s是包含多个小数的字符串，由逗号隔开，如s = '1.23, 2.4, 3.123'。编写一个程序，输出s中所有数值的和。
# s = '1.23, 2.4, 3.123'  # 给定的包含小数的字符串

# # 将字符串按逗号分割成小数字符串列表
# decimal_strings = s.split(',')

# # 初始化一个变量来存储总和
# total_sum = 0

# # 遍历小数字符串列表，将每个字符串转换为浮点数并累加到总和
# for decimal_string in decimal_strings:
#     number = float(decimal_string.strip())  # 去除空格并转换为浮点数
#     total_sum += number

# # 输出总和
# print("所有数值的和:", total_sum)
