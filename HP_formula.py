'''
 # @ Author: Jeff Chen
 # @ Create Time: 2023-12-29 14:10:14
 # @ Description: 公式基础函数库
 '''
"""
模仿通达信公式，转为python函数的过程：
1. `:=`是赋值语句，替换为python的`=`
2. `:`是公式的赋值带输出画线命令，替换为`=`，它之前为输出变量，顺序写到return的返回参赛中
3. 全部命令转为英文大写
4. 删除绘图格式命令
5. 删除每行末的分号
6. 参数可写到函数参数表中，例如: def KDJ(N=9, M1=3, M2=3):

举例，通达信KDJ指标公式如下：
参数表 N:=9, M1:=3, M2:=3
RSV:= (CLOSE - LLV(LOW, N)) / (HHV(HIGH, N) - LLV(LOW, N)) * 100;
K: SMA(RSV, M1, 1);
D: SMA(K, M2, 1);
J: 3 * K - 2 * D;

# 转换为python函数如下：
def KDJ(N=9, M1=3, M2=3):
    RSV = (CLOSE - LLV(LOW, N)) / (HHV(HIGH, N) - LLV(LOW, N)) * 100
    K = SMA(RSV, M1, 1)
    D = SMA(K, M2, 1)
    J = 3 * K - 2 * D
    
    return K, D, J
"""

import pandas as pd
import numpy as np
import HP_global as g


# 平均函数
def MA(Series, N):
    return pd.Series.rolling(Series, N).mean()


def SMA(Series, N, M=1):
    ret =[]
    i = 1
    length = len(Series)
    
    # 跳过X中前面的几个nan值
    while i<length:
        if np.isnan(Series.iloc[i]):
            i += 1
        else:
            break
    
    preY = Series.iloc[i]   # Y轴
    ret.append(preY)
    
    while i<length:
        Y = (M * Series.iloc[i] + (N - M) * preY) / float(N)
        ret.append(Y)
        preY = Y
        i += 1
        
    return pd.Series(ret, index=Series.tail(len(ret)).index)


def HHV(Series, N):
    return pd.Series(Series).rolling(N).max()


def LLV(Series, N):
    return pd.Series(Series).rolling(N).min()


# def KDJ(N=9, M1=3, M2=3):
    
#     RSV = (CLOSE - LLV(LOW, N)) / (HHV(HIGH, N) - LLV(LOW, N)) * 100
#     K = SMA(RSV, M1, 1)
#     D = SMA(K, M2, 1)
#     J = 3 * K - 2 * D
    
#     return K, D, J


# 测试用例
if __name__ == '__main__':

    print('end')