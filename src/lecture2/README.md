# TOPICS

**Branching and Iteration**

# READINGS

**Chapters 2.2, 2.3.1, 2.4, and 3.2**

**2.3 字符串和输入**

- str类型的对象用来表示由字符组成的字符串
- 操作符+被称为重载

```
>>> str('a')
>>> 'a'
>>> 3*'a' # 'aaa'
```

- 表达式n * s (n是一个int对象，s是一个str对象，表达式的值就是一个将s重复n次的str对象)
- len函数求出字符串的长度, len(abc), 值为3
- 使用索引从字符串提取单个字符, 'abc'[0], 值为'a', 'abc'[-1]的值是'c'
- 分片操作从字符串提取任意长度的子,s[start:end], s[:],

```

>>> 'a'*'a' # error
>>> a # error
>>> '4' < 3 # error
>>> 'abc'[1:3] # 'bc'

```

**2.3.1: 输入**

- input函数, 等待用户输入，用户输入以回车键结束
- 当print语句有多个参数时，会在每个参数对应的值之间加上一个空格, 使用连接生成一个没有多 余空格的字符串
- input函数,参数默认为字符串String
- 使用类型名称将一个值转换为这种类型, int('3'), int(3.9)的值都为3

```

>>> print('Are you really', name, '?')
Are you really George Washington ?
>>> print('Are you really ' + name + '?')
Are you really George Washington?
int('3') * 4 # 12
int(3.9) # 3

```

**2.3.2 字符编码**

- 多数编程语言都使用一种名为ASCII的标准,这个标准 包括128个字符
- 最近几年，人们逐渐转向Unicode, 这个标准中的字符超过120000个, 覆盖了129种从古至今的语言和符号集合

```

# 如果在程序中找不到这样的注释，多数Python实现会默认使用UTF-8

# -*- coding: utf-8 -*-

```

**Chapters ???: Comparisons**

**2.2: Branching 条件语句**

- 最简单的分支语句是条件语句
- 缩进在Python中是具有语义意义的
-

```

# 在条件语句的检验条件中，使用复合布尔表达式是非常方便的

# Boolean expression 它的取值为True或False

if Boolean expression:
    block of code
elif Boolean expression:
     block of code
else:
    block of code

```

**Chapters 2.4 : While Loops 迭代(也称循环)**

- 需要程序多次做同一件事情的时候，可以使用迭代语句
- 与条件语句类似，它从一个测试条件开始。如果测试条件取值为True，程序 就执行一次循环体，然后重新检查测试条件。一直重复这个过程
- 使用break语句结束它所在的循环
- 如果在嵌套的循环语句(位于另一个循环语句内部的循环语句)中执行break语句，那么
break语句会结束内层循环语句。

**3.2 : For Loops**

- 序列值通常使用内置函数range生成
- range函数接受3个整数参数:start、stop和step
- 如果step是正数，最后一个元素就是小于stop的最大整数start + i * step
  - range(5, 40, 10)
  - 5, 15, 25, 35
- 如果step 是负数，最后一个元素就是大于stop的最小整数start + i * step
  - range(40, 5, -10)
  - 40, 30, 20, 10

```
x=4
for i in range(0, x):
    print(i) 

total = 0
for c in '12345678':
    total = total + int(c)
print(total)
```
