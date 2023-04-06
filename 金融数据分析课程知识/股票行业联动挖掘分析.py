import pandas as pd
codename=pd.read_excel('指数基本信息表.xlsx')
sname=pd.Series(list(codename.iloc[:,1]),index=codename.iloc[:,0])
data=pd.read_excel('指数交易数据表20100104-20170307.xlsx')
code_record=data.iloc[:,0].value_counts()
code=list(code_record[code_record==1741].index)
import numpy as np
D=dict()
for t in range(len(code)):
    dt=data.loc[data ['指数代码']==code[t],['交易日期','收盘价']].sort_values('交易日期')
    dtl=dt.iloc[0:-1,[1]]['收盘价']
    dt2=dt.iloc[1:,[1]]['收盘价']
    z21_up=np.zeros(len(dtl))
    z21_up[dt2.values-dtl.values>0]=1
    D.setdefault(sname[code[t]]+'_up',z21_up)
    
td=pd.read_excel('交易日历数据表.xlsx')
Data=pd.DataFrame(D,index=td['Clddt'].values[1:1741])
import apriori as ap
support =0.47 #最小支持度
confidence = 0.9 #最小置信度
ms='--' #连接符， #结果文件
outputfile='日行业联动挖掘.xlsx' #联动
ap.find_rule(Data, support, confidence, ms).to_excel(outputfile)
'''
import OneRule as OR
r = OR.rule(Data,0.3,0.59)
'''
