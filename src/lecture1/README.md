# TOPICS
**What is computation?**

# READINGS
**Chapters 1 and 2.1**

**Chapters 1**
- 计算机能且只能做两件事，执行计算与保存计算结果
- 编程基本思想的核心仍然是组装操作序列的过程。
- 每种编程语言都有基本结构、语法、静态语义和语义
- 算法的定义
算法是一个有穷指令序列，描述了这样一种计算过程，即在给定的输入 集合中执行时，会按照一系列定义明确的状态进行，最终产生一个输出结果。

**Chapters 2.1**
- 吉多·范·罗苏姆1990年发明Python
- 2000年Python推出2.0版本
- Python 3.0在2008年末发布, 它不是向后兼容的

# Python 基本元素
- Python程序有时称为脚本，是一系列定义和命令
- Python解释器，有时称为shell，用来求值 这些定义并执行命令
- 命令通常称为语句，用来指示解释器做一些事情

## 对象、表达式和数值类型
- 对象是Python程序处理的核心元素
- 类型分为标量和非标量(标量对象是不可分的，可以把它们视为语言中的原子)

### Python有以下4类标量对象
- int 整数
- float 实数, 浮点数
- bool 布尔值, True or False
- None

1. Python内置函数type - 检测对象类型
```
>>> type(3)
<type 'int'>
>>> type(3.0)
<type 'float'>
```
2. int类型和float类型 - 表达式支持的操作符
```
i + j # 都是int类型, 结果才是int
i - j # 同上
i * j # 同上
i // j # 整数除法, 6 // 4 的值是 1, j = 0 报错
i / j # 浮点数除法
i % j # 余数
i ** j # i的j次方, 都是int类型, 结果才是int
# 比较运算符包括:
# ==(等于)、!=(不等于)、>(大于)、>=(大于等于)、<(小于) 和<=(小于等于)
```
3. bool类型上的基本操作符为and、or和not
```
 a and b # 都为True时,值为True
 a or b # a和b至少一个True, 值为true
 not a # a为False, 值为True, 反之亦然
```

## 变量和赋值
- 变量将名称与对象关联起来
- 在Python中，变量仅是名称，没有其他意义(恰当地选择变量名称可以增强程序可读性)
- 赋值语句将=左边的名称与=右边的表达式所表示的对象关联起来
- 一个对象可以有一个或多个名称与之关联，也可以不关联任何名称
```
 pi = 3
 radius = 11
 area = pi * (radius**2)
 radius = 14

 # pi -> 3
 # radius -> 11
 # area -> 363
 # radius -> 14 名称radius就被重新绑定到一个新的int类型的对象, !!这次赋值对area绑定的值没有影响
```
1. 变量的命名规则
- 包含大写字母、小写字母、数字(但不能以数字开头)和特殊字符_
- Python变量名是大小写敏感的
- 保留字(有时称为关键字), 有专门的意义，不能用作变量名
  - and、as、assert、break、class、 continue、def、del、elif、else、except、False、finally、for、from、global、if、 import、in、is、lambda、nonlocal、None、not、or、pass、raise、return、True、try、 while、with和 yield
2. 添加注释, Python不解释符号#后面的文本
3. 多重赋值
```
x, y = 2, 3
x, y = y, x
print ('x =', x)
print ('y =', y)

# 输出
# x = 3
# y = 2
```