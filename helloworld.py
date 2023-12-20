import decimal
print('''This is a multi-line string. This is the first line.
This is the second line.
"What's your name?" I asked.
He said "Bond,James Bond."
''')

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

# **
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

#
# print(dir(decimal))
# print(dir(print))

# import math
# print(pi)
# print(math.pi)
# print(dir(math))

# 
languages = ['Python', 'R', 'Matlab', 'C++']
a = list(enumerate(languages,1))
print(type(a[1]))

# list
list_1 = [1,2,3,"four"]
print(list_1,type(list_1),type(list_1[0]),type(list_1[3]))

x = [[0]*3]*4
print(x,type(x),str(id(x[0])),str(id(x[1])))
x[1][0]=1
print(x,type(x),str(id(x[0])),str(id(x[1])))




