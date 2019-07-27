import numpy as np
# a = np.arange(1,8,2)#整数序列左闭右开
# print(a.dtype)
# print(a.size)
# a= np.linspace(2,10)#等差数列




# a= np.random.rand(10)#随机浮点数
# b= np.random.randn(10)#正态分布
# c= np.random.randnit(10)



# m = np.array([np.arange(2),np.arange(2)])
# print(m)
# print(m.shape)

# print(bool(-1))

#指定函数参数的数据类型,复数是不能转换为整数,浮点数但反过来可以
# x = np.arange(7, dtype=np.uint16)
# # #转换数据类型
# # x = x.astype('float')
# # print(x)

# a = np.arange(24).reshape(2,3,4)#改变维度
# a.shape = (6,4)#改变维度
# resize 和 reshape 函数的功能一样，但 resize 会直接修改所操作的数组
# print(a)
# a.ravel()#展开数组，只是返回数组的一个视图（view）
# a.flatten()#展开数组，会请求分配内存保存结果


#索引（python是引用机制）

#花式索引(返回的是复制不是引用)
# a = np.arange(10,100,10)
# print(a)
# index = np.array([1,2,6])
# mask = np.array([0,1,1,0,0,0,1,0,0],dtype=bool)
# print(a[index])
# print(a[mask])
#二维数组花式索引
# b = np.array([[1,2,3,4,5],[6,7,8,9,10]])
# index1 = (0,0),(1,1)
# index2 =[0,0],[1,1]
# print(b[index1])
# print(b[index2])


#类型转换
# a= np.array([1,2,3])
# print(np.asarray(a,dtype=float))
# print(a.astype(float))


#数组操作
#数组排序
# np.sort(a)
# np.argsort(a)

# list1 = [1,2,3]
list1 = [[1,2],[3]]
list2 = list1.copy()
l
print(list1)
print(list2)