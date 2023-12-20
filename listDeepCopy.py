i = 77
j = 76

print('i id : ',id(i))
print('j id : ',id(j))

j+=1
print('j id : ',id(j))

a = "hello"
b = "hello"

print(a is b , a == b)

vad = [[140, 29880], [30350, 31820], [31820, 50350]]
new_vad = [] 

print("vad: ",vad)
for i in range(len(vad)):
    if i == 0:
        new_vad.append(vad[i])
    else:
        # print("new_vad: ",new_vad)
        # print("vad: ",vad)
        if vad[i][0] == new_vad[-1][1]:
            new_vad[-1][1] = vad[i][1]
        else:
            new_vad.append(vad[i])
print("vad: ",vad)
# print("new_vad : ",new_vad)