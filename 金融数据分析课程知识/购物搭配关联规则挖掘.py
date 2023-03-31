#item应该从data中提取的
item = ['西红柿','排骨','鸡蛋','茄子','袜子','酸奶','土豆','鞋子']
import pandas as pd
import numpy as np
#header = None 属性可以将第一行数据加载到第二行，第一行就是index 1 2 3 ect.
data = pd.read_excel('tr.xlsx',header = None)

#删去I1 I2 I3第一列这些项集的编号
data = data.iloc[:,1:]

#为啥创建D呢？
D = dict()

for i in range (len(item)):
  for t in range (len(item)):
    z = np.zeros(len(data))
    li = list()
    for k in range(len(data.iloc[0,:])):
        s=data.iloc[:,k]==item[t]
        li.extend(list(s[s.values == True].index))
    z[li]=1
    D.setdefault(item[t],z)
Data = pd.DataFrame(D)
c= list(Data.columns)
c0=0.5
s0=0.2
list1 = []
list2 = []
list3 = []
for k in range(len(c)):
    for q in range(len(c)):
        # 对第c[k]个项与第c[q]个项挖掘关联规则，前件为c[k]，后件为c[q]，且要求前件和后件不相等
        if c[k] != c[q]:
            c1 = Data[c[k]]
            c2 = Data[c[q]]
            I1 = c1.values == 1
            I2 = c2.values == 1
            t12 = np.zeros((len(c1)))
            t1 = np.zeros((len(c1)))
            t12[I1 & I2] = 1
            t1[I1] = 1
            sp = sum(t12) / len(c1)  # 支持度
            co = sum(t12) / sum(t1)  # 置信度
            # 取置信度大于等于C0的关联规则
            if co >= c0 and sp >= s0:
                list1.append(c[k] + '--' + c[q])
                list2.append(sp)
                list3.append(co)
R = {'rule':list1,'support':list2,'confidence':list3}

R = pd.DataFrame(R)
R.to_excel('rule2.xlsx')
  
