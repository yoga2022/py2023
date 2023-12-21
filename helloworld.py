import decimal
#string
print('''This is a multi-line string. This is the first line.
This is the second line.
"What's your name?" I asked.
He said "Bond,James Bond."
''')

#print
print('{:.2f}'.format(1.0/3))
print('{:_^13}'.format('hello'))
print('{name} wrote {book}'.format(name='a',book='b'))
print('a',end=" ")
print('b',end=" ")
print('What\'s your name?')
print('This is the first line\nThis is the second line.')
print(r'This \n')

#TODO 按位取反
print(bin(~4)) 
#三元运算符
x,y = 4,5
small = x if x < y else y
print(small)

# 运算符** 
print((-3)**2)
# 优先级
print(1 << 3+2 | 7) #100000 0111

#
set_1 = {"欢迎","来到","2024"}
print(set_1.pop()) 
print(set_1.pop())
print(set_1.pop())
print(str(set_1))

#
# print(type(1.2e-5))

# dir 万物皆可对象
# print(dir(decimal))
# print(dir(print))
# import math
# print(pi)
# print(math.pi)
# print(dir(math))









