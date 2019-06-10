# 元素分类 有如下值集合 [11,22,33,44,55,66,77,88,99]，
# 将所有大于 66 的值保存至字典的第一个 key 中，将小于 66 的值保存至第二个 key 的值中
# 即: {‘k1’: 大于 66 的所有值, ‘k2’: 小于 66 的所有值}
list1=[11,22,33,44,55,66,77,88,99]
list2=[]
list3=[]
dic1={}
for i in list1:
    if i>66:
        list2.append(i)
    elif i<66:
        list3.append(i)

dic1['k1']=list2
dic1['k2']=list3
print(dic1)