
```
import numpy as np
import matplotlib.pyplot as plt
```

# plt.plot
1. 原则上plt.plot绘图需要x轴和y轴信息，但是当传入的y轴数据是dnarray是，x轴会自动取值range(len(y)), 所有没必要再提供x轴信息
2. 一般来说，讲二维数组传递给plt.plot时，它会自动把包含的数据解释为单独的数据集（沿着Y轴，即第二维）

# plt.bar
1. plt.bar 用于画出柱状图
2. 必须提供X轴、Y轴的数据
```
'''
Created on Nov 17, 2018

@author: evanli
'''


import numpy as np
import matplotlib.pyplot as plt
# %matplotlib inline

def book512():
    np.random.seed(2000)
    y = np.random.standard_normal((20,2)).cumsum(axis=0)
#    y = np.array([[1,2,3,4,5,6], [11,12,13,14,15,16]])
#   y = np.array([[1],[2],[3],[4],[5],[6])
    plt.figure(figsize = (9,4))
    plt.subplot(121)
    plt.plot(y[:,0],'b', label='1st') #先画上线，label是图例的命令
    plt.plot(y[:,0],'ro')  #再画上红点
    plt.grid(True)
    plt.legend(loc=0)
    plt.axis('tight')
    plt.xlabel('index')
    plt.ylabel('value')
    plt.title('1st Data Set')
    
    plt.subplot(122)
    plt.bar(np.arange(len(y)), y[:,1],width=0.5,color='g',label='2nd')
    print(np.arange(len(y)))
    plt.grid(True)
    plt.legend(loc=0)
    plt.axis('tight')
    plt.xlabel('index')
    plt.title('2nd Data Set')
        
     
    plt.show()
    
  
book512()  
```
