import OneRule as OR
r = OR.rule(Data,0.3,0.59)
'''qiche--zonghe zhichidu zhixindu'''
#一★- coding: utf-8一★一
defrule(Data,s0,c0):
#获取字段名称(行业名称 up)，并转化为列表
import numpy as np
import pandas as pd
c=list(Data.columns)
list1=[]#预定义定义列表list1，用于存放规则
list2=[]#预定义定义列表list2，用于存放规则的支持度list3=[]#预定义定义列表
list3=[]用于存放规则的置信度
for kin range(len(c)):
for qinrange(len(c)):
#对第c[k]个行业与第c[q]个行业计算行业轮动规则#规则的前件为c[k]
是把微的有6921，计算周期与]需后移一个周期c2=Data[c[q]][1:]
I1=c1.values==1
I2=c2.values==1
t12=np.zeros((len(c1)))
t1=np.zeros((len(c1)))
t12[I1&I2]=1
sp=sun(t12)
t1[I1]=1
/len(c1) #支持度
co=sum(t12)/sum(t1) #置信度
if co>c0 and sp>s0:
list1.append(c[k]+'--'+c[q])
list2.append(sp)
list3.append(co)
#定义字典，用于存放关联规则及其置信度、支持度R=('rule':list1,'support':list2,'confidence':list3#将字典转化为数据框
R=pd.DataFrame(R)
#将结果导出到Excel
R.to excel('R.x1sx')
return R
