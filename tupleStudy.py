t1 = (1,10.31,'python')
t2 = 1,10.31,'python'
print(t1,type(t1))
print(t2,type(t2))
print(t1 is t2)
print(t1==t2)
#注意：元组使用for-range时：
t3 = tuple(i for i in range(10))
print(t3,type(t3))
print(t3[1])
print(t3[:-5])
print(t3[8:6:-1])
t4 = t3[:]
print(t4,type(t4))
#元组只包含一个元素时，需要在元素后面加逗号，否则括号会被当作运算符使用
x = (1) 
print(x,type(x))
x = ()
print(x,type(x))
x = (1,)
print(x,type(x))
print(2*(2))
print(2*(2,))
#二元元组
t5 = (1,10.31,'python'),('data',11)
print(t5,type(t5))
print(t5[0])
print(t5[0][0],t5[0][1])
print(t5[0][1:])
#元组的更新和删除
#元组不可更改（immutable），不能直接给元组的元素赋值，但是只要元组中的元素（mutable），可以直接更改其元素
week = ('Monday', 'Tuesday', 'Thursday', 'Friday')
week = week[:2]+("Wednesday",)+week[2:]
print(week)
t6 = (1,2,3,[4,5,6])
t6[3][0] = 9
print(t6)
#操作符 == 、+、*、in、not in均与list相同
t7 = (123,456)
t8 = (456,123)
t9 = t7+t8
print("t9:",t9)
t7 = t7[:1]+(789,)+t7[1:]
print("t7:",t7)
print("t9:",t9)
#count、index用法同list。因为元组大小内容不可更改，所以只能用这两种方法
print(t7.count(123))
print(t9.index(456))
#解压元组（unpack）
(a,b,c) = t1
print(a,b,c)
t10 = (1, 'python',(4,5))
(a,b,(c,d)) = t10
print(a,b,c,d)
#如果只要元组其中几个元素，用通配符* （wildcard），代表一个或多个元素。
a,b,*rest,c = t3
print(a,b,c)
print(rest,type(rest))
a,*rest = t10
print('源:',t10,"保留:",a,"*rest:",rest,"rest class:",type(rest))
a,*_ = t10
print(a) #根本不在乎 *里面的值
