import pandas as pd

# 读取数据
td = pd.read_excel('index300.xlsx')

# 构造特征(指标)

# A1(收盘价/均价)收盘价/过去10个交易日的移动平均收盘价
A1 = td['Idxtrd05'].values / td['Idxtrd05'].rolling(10).mean()

# A2（现量/品）成交量 / 过去10个交易日的移动平均成交量
A2 = td['Idxtrd06'].values / td['Idxtrd06'].rolling(10).mean()

# A3（收益率）当日收盘价前日收盘价）/应日收盘价
A3 = td['Idxtrd08'].values

# A4（最高价-均价）/过去10个交易日的移动平均收盘价
A4 = td['Idxtrd03'].values / td['Idxtrd03'].rolling(10).mean()

# A5（最低价-均价）/过去10个交易日的移动平均收盘价
A5 = td['Idxtrd04'].values / td['Idxtrd04'].rolling(10).mean()

# A6(极差)最高价-最低价（衡量波动性）
A6 = td['Idxtrd03'].values - td['Idxtrd04'].values

# A7（涨跌幅大小）当日收盘价-前日收盘价
A7 = td['Idxtrd05'].values - td['Idxtrd02'].values

# 构造数据的X部分
X = {'A1': A1, 'A2': A2, 'A3': A3, 'A4': A4, 'A5': A5, 'A6': A6, 'A7': A7}
X = pd.DataFrame(X)
# 取第10行到倒数第2行
X = X.iloc[9:-1]

# 构造数据的Y部分
Y = td['Idxtrd05'].values[1:]-td['Idxtrd05'].values[:-1]
Y = Y[9:]
Y[Y>0]=1
Y[Y<=0]=-1
# 为什么这里从第9行开始取？
# 因为在构造特征时，使用了10个交易

x_train=X.iloc[:len(X)-30,:]
y_train = Y[:len(Y)-30]

x_test=X.iloc[len(X)-30:,:]
y_test=Y[len(Y)-30:]



from sklearn import svm

# 构造SVM的分类模型
clf = svm.SVC(C=0.1)

# 在训练数据上训练分类器
clf.fit(x_train, y_train)

# 在训练集上计算分类器的ACC
svc_acc_train = clf.score(x_train, y_train)

# 在测试集上预测结果
R = clf.predict(x_test)
R = R.reshape(len(R), 1)
Z = R - y_test
Rs1 = len(Z[Z == 0]) / len(Z)

'''
差三页ppt
'''
