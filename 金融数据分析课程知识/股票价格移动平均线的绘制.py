import pandas as pd
import numpy as np
#导入python绘图包
import matplotlib.pyplot as plt

#trd中存有股票代码，日期，该天价格
trd = pd.read_excle('股票价格移动.xlsx')

#使用count计数（除代码为2012股票为11次，其他均出现63次）
c = trd['Strkcd'].value_count()

#统计股票种类，共0-19，20只股票
code=list(c.index)

#动态计算需要q个figure，其中每个figure绘制4个子图，每个子图代表一个股票，在子
#初始值设置q=0
q=0

#循环对每一个股票绘制其图形（这里知道len(c)=20，即20只股票，也即将会生成20个小图）
for i in range(20):
  
  #第i个股票代码的收盘价，记为p,并计算其移动平均价(Moving Average MA5表示过去5天（含今天）的价格的平均数)
  #并构造绘图的x,y值
  sp=trd.loc[trd['Stkcd'].values==code[i],'Clsprc']
  p = sp.values
    avg_p=sp.rolling(10).mean()
    x1=np.arange(0,len(p))
    y1=p
    y2=avg_p[9:]
    x2=np.arange(9,len(p))
  
    #如果i与4整除，代表需要重新建一个figure（因为每个figure有4个子图），q在这里发挥作用：充分利用一张A4纸画四个图。
    if i%4==0: 
        q=q+1                    
        plt.figure(q)               
        plt.figure(figsize=(8,6))      
    plt.subplot(2,2,i%4+1)
    
    #用于设置图像外部边缘自动调整
    plt.tight_layout() 
    
    #一张图上会出现两条趋势有点像的折线，不过其中一条从第十个x开始，即移动平均线。
    plt.plot(x1,y1)
    plt.plot(x2,y2)
    
    #将该图片储存在同一任务目录下
    plt.savefig(str(q))
  
