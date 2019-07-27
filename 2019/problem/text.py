
list1 = []
# list2 = []
# for i in range(2):
#     list2 += [0]
list2 = [0,0]
for i in range(2):
    list1.append(list2)

print(list1)
list1[0][0]=1
print(list1)



list3 = []
for i in range(2):
    list3.append([0,0])
print(list3)
list3[0][0] = 1
print(list3)
