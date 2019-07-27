import pandas as pd
import numpy as np
import xlrd
# date = pd.date_range('20190702',periods=6)
# print(date)
# d = np.random.randn(6,4)
# df = pd.DataFrame(d)
# print(d)
# print(df)


# df2 = pd.DataFrame({'A':pd.Series(1,index=list(range(4)),dtype=float),'B':pd.Categorical(['a','b','c','d'])})



df = pd.read_excel(r'E:\Tencent Files\FileRecv\data.xlsx')
# print(df.head())#前五行
# print(df.iloc[0:5])#左闭右开
# print(df.loc[0:5])#左右闭合

#标签选择数据
# df.loc[1,'名字']#行号，列名
# df.loc[[1,3,4,7],['名字','评分']]

#缺失值/异常值处理

#行操作
#添加s =pd.serious({ })
# df = df.apprned(s)
#删除df = df.drop([300])

#列操作
# df.columns()#查看所有列名
# df['名字']#查看名字这一列的数据

#增加
# df['序号'] = range(1,len(df)+1)
# 删除
# df = df.drop('序号',axis=1)#axis表示方向默认等于0代表横向，等于1代表纵向