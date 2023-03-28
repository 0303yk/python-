# -*- coding: utf-8 -*-
import pandas as pd
Data=pd.read_excel('农村居民人均可支配收入来源2016.xlsx')
#取出所有列（有四个指标）
X = Data.iloc[:,1:]
#计算各指标的相关系数
R = X.corr()

# 数据规范化处理
from sklearn.preprocessing import StandarScaler
scaler = StandarScaler()
#标准化处理
scaler.fit(X)
#数据变为更小的数
X = scaler.transform(X)

#主成分分析
from sklearn.decomposition import PCA

#整数就是指标的个数，小数为指标比例
pca = PCA(n_components=0.95)

#Y中有三个指标（使得原指标之间互不相关）
pca.fit(X)
Y=pca.transform(X)
py=pd.DataFrame(Y).corr()

#下面操作得到创建的指标Y获得权重
tzxl=pca.components_              
tz=pca.explained_variance_          
gxl=pca.explained_variance_ratio_

'''
#以下是检验分别为
4.3358839429206855
1.5373620336578577
-0.46694468480762524
-0.10431270770219253
'''

Y00=sum(X[0,:]*tzxl[0,:])
Y01=sum(X[1,:]*tzxl[0,:])
Y02=sum(X[2,:]*tzxl[0,:])
Y03=sum(X[3,:]*tzxl[0,:])

#主成分分析步骤结束，综合排名(综合得分=各个主成分*贡献率之和)
F=gxl[0]*Y[:,0]+gxl[1]*Y[:,1]+gxl[2]*Y[:,2]

#提取地区
dq=list(Data['地区'].values)

#以地区作为index，综合得分为值，构建序列
Rs=pd.Series(F,index=dq)

#按综合得分降序进行排序
Rs=Rs.sort_values(ascending=False) 

'''
结果如下：
北京	3.038413004497421
上海	2.582823454980638
天津	1.4466764648710317
浙江	1.2605431754949288
...
'''
