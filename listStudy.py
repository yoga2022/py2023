# list

# enumerate 带索引的显示列表 
languages = ['Python', 'R', 'Matlab', 'C++']
a = list(enumerate(languages,1))
print(type(a[1]))


list_1 = [1,2,3,"four"]
print(list_1,type(list_1),type(list_1[0]),type(list_1[3]))

list_2 = [[0]*3]*4
print(list_2,type(list_2),str(id(list_2[0])),str(id(list_2[1])))
list_2[1][0]=1
print(list_2,type(list_2),str(id(list_2[0])),str(id(list_2[1])))

#list extend
list_1.extend(["five","six","seven","eight","nine"])
print(list_1)
#list append
list_1.append("ten")
print(list_1)

#list remove
list_1.remove("six")
print(list_1)
#list pop
list_1.pop()
print(list_1)
#list del 如果你要从列表中删除一个元素，且不再以任何方式使用它，就使用del语句；如果你要在删除元素后还能继续使用它，就使用方法pop()。
del list_1[0:2]
print(list_1)
#切片
print(list_1[:-3:-1])
#注意第一个元素和第二个元素的大小关系
print("逆序step:",list_1[-1:-4:-1])
#list运算符
list1 = [12,34]
list2 = [34,12]
list3 = [12,34]
print(list2==list3)
print(list3==list1)
#前面三种方法（append, extend, insert）可对列表增加元素，它们没有返回值，是直接修改了原数据对象。 而将两个list相加，需要创建新的 list 对象，从而需要消耗额外的内存，特别是当 list 较大时，尽量不要使用 “+” 来添加list。
list4 = list1+list2 
print(list4)
list5 = list3*3
print(list5)
list5[0] = 8
print(list3)
list3 *= 3
print(list1)
print(list3)
print(list5)
print(12 in list3)
print(34 not in list3)
list6 = [[12,3],[45,6]]
list7 = [[45,6],[12,3]]
list8 = list6+list7
#深拷贝
list7[0][0] = 12
print(list8)
#list count 统计某个元素在列表中出现的次数
print(list8.count([12,3]))
#list index 从列表中找出某个值第一个匹配项的索引位置 后两个参数开始-结束下标。最终返回结果是原数组的下标
list9 = [1,11,111,1111,11111,1111,111,11,1,11,111,1111,11111,1111,111,11,1,11,111,1111]
print(list9.index(1))
print(list9.index(1,1))
print(list9.index(1,9,17))
#list reverse 反向列表中元素
list9.reverse()
print(list9)
#list sort list.sort(key=None, reverse=False) 对原列表进行排序。
# key -- 主要是用来进行比较的元素，只有一个参数，具体的函数的参数就是取自于可迭代对象中，指定可迭代对象中的一个元素来进行排序。
# reverse -- 排序规则，reverse = True 降序， reverse = False 升序（默认）。
# 该方法没有返回值，但是会对列表的对象进行排序。
list9.sort(reverse=False)
print(list9)
print(list8)
def takeSecond(elem):
    return elem[1]
list8.sort(key=takeSecond)
print(list8)
#lambda a:a[0]匿名函数，他接受列表中每个元素`a`并返回`a[0]`，即每个元素的第一个元素。
#排序将根据每个元素的第一个元素进行
list8.sort(key=lambda a:a[0])
print(list8)