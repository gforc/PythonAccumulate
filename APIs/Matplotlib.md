
```
import numpy as np
import matplotlib.pyplot as plt
```

# plt.plot 线状图
1. 原则上plt.plot绘图需要x轴和y轴信息，但是当传入的y轴数据是dnarray是，x轴会自动取值range(len(y)), 所有没必要再提供x轴信息
2. 一般来说，讲二维数组传递给plt.plot时，它会自动把包含的数据解释为单独的数据集（沿着Y轴，即第二维）

# plt.bar 柱状图
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
    plt.figure(figsize = (9,4)) #制定图表大小
    plt.subplot(121) #设置子图的位置 plt.subplot(总行数，总列数，子图编号)
    plt.plot(y[:,0],'b', label='1st') #先画上线，label是图例的名称
    plt.plot(y[:,0],'ro')  #再画上红点
    plt.grid(True) #enable 网格
    plt.legend(loc=0) # 设置图例，0表示最佳位置
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

# plt.hist 离散点
```
def book513_2():
    y = np.random.standard_normal((100,2))
#    y = np.array([[1,2,3,4,5,6], [11,12,13,14,15,16]])    
#    y = np.array([[1,2],[3,4],[5,6],[7,8],[9,10],[1,2],[3,4]])
    plt.figure(figsize= (10,8))
    plt.subplot(121)
    plt.hist(y, label=['1st','2nd'],bins =10)
    plt.grid(True)
    plt.legend(loc=0)
    plt.xlabel('value')
    plt.ylabel('frequency')
    
    plt.subplot(122)
    plt.hist(y,label=['1st','2nd'],bins = 10, color=['b','g'], stacked=True)
    plt.grid(True)
    plt.legend(loc=0)
    plt.xlabel('value')
    plt.xlabel('frequency')
    plt.title('Histogram')
     
    plt.show()
    
```



# 求函数面积
```
def book513_4():
    a, b = 0.5, 1.5
    x= np.linspace(0,2)# linespace 产生等差数列，从0到2产生50（default）个元素
    y = func(x)
    
    fig, ax = plt.subplots(figsize=(7,5))
    plt.plot(x,y,'b', linewidth=2)
    plt.ylim(ymin=0)
    
    Ix = np.linspace(a,b)
    Iy = func(Ix)
    verts = [(a,0)]+list(zip(Ix,Iy)) + [(b,0)]  ##确定多边形的几个顶点
    poly = Polygon(verts, facecolor='0.7', edgecolor='0.5')  ##多边形函数polygon
    ax.add_patch(poly)
    
    plt.text(0.5*(a+b),1,r"$\int_a^b f(x)\mathrm{d}x$", horizontalalignment='center', fontsize=20) #图中显示文本的坐标（0.5*(a+b),1）和内容，此处的坐标是坐标轴的坐标
    plt.figtext(0.9, 0.075, '$x$') #图中显示文本的坐标（0.9，0.075）和内容，此处的坐标是相对figure的坐标
    plt.figtext(0.075,0.9,'$f(x)$')
    
    ax.set_xticks((a,b))  #设置x轴刻度位置
    ax.set_xticklabels(('$a$', '$b$')) #设置x轴刻度名称
    ax.set_yticks([func(a),func(b)])  #设置y轴刻度位置
    ax.set_yticklabels(('$f(a)$','$f(b)$'))#设置y轴刻度名称
    plt.grid(True)
    
    plt.show()
```

