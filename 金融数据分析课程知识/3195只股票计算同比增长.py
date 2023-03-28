'''
问题如下：对每个股票代码，计算每个季度每股收益同比增长率
其中 Stked 为股票代码，Accper 为截止日期，F090301B为归属于母公司每股收益，F090601B为每股营业收入，F091001A为每股净资产，F091301A为每股资本公积，F091501A为每股未分配利润，F091801B为每股经营活动产生的现金流量净额。
同比=（今年这个月-去年这个月）/去年这个月*100%
'''
# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
A=pd.read_excel('3195只股票数据.xlsx')

#表示对第0列（Stkcd）的种类进行统计
s = A.iloc[:,0].value_counts()

#挑选出出现8次的股票的种类（即股票代码名称）
code = list(s[s==8].index)

#遍历每一只股票代码，计算同比收益率,所以这步干嘛的？
#哦，创建了一个空的code行，4列的array
rets = np.zeros((len(code),4))
for i in range(len(code)):
    A3 = A.iloc[A.iloc[:,0].values==code[i],2].values
    r = (A3[-4:]-A3[:4])/A3[:4]
    rets[i] = r

rets_data = pd.DataFrame(rets,index = code)
rets_data.to_excel("rets.xlsx")   
