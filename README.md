# PythonAccumulate



# Python APIs

## ZIP
zip()是Python的一个内建函数，它接受一系列可迭代的对象作为参数，将对象中对应的元素打包成一个个tuple（元组），然后返回由这些tuples组成的list（列表）。
若传入参数的长度不等，则返回list的长度和参数中长度最短的对象相同。利用*号操作符，可以将list unzip（解压）。
```
list1 = [1,2,3,4]
list2 = [5,6,7,8]
print zip(list1,list2) 
#输出结果是   [(1, 5), (2, 6), (3, 7), (4, 8)]
```

```
str1 = "abcd"
str2 = "123456"
print zip(str1,str2)
输出结果是：[('a', '1'), ('b', '2'), ('c', '3'), ('d', '4')]
```

```
a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
 print zip(*a)  输出结果是：[(1, 4, 7), (2, 5, 8), (3, 6, 9)]
 ```



## round()
round()方法返回 x 的小数点四舍五入到n个数字。
```
print “round(80.23456, 2) : “, round(80.23456, 2) 
print “round(100.000056, 3) : “, round(100.000056, 3) 
print “round(-100.000056, 3) : “, round(-100.000056, 3) 

#当我们运行上面的程序，它会产生以下结果：
round(80.23456, 2) : 80.23 
round(100.000056, 3) : 100.0 
round(-100.000056, 3) : -100.0
```

# Signal

信号的概念
信号（signal）--     进程之间通讯的方式，是一种软件中断。一个进程一旦接收到信号就会打断原来的程序执行流程来处理信号。

几个常用信号:

SIGINT     终止进程  中断进程  (control+c)

SIGTERM   终止进程     软件终止信号

SIGKILL   终止进程     杀死进程

SIGALRM 闹钟信号


```
import signal
import os
from time import sleep

def handle_method(signal, frame):   # 注意函数所带的参数
    print 'do something'

signal.signal(signal.SIGINT, handle_method)


while 1:
    print 'my process ID is %s' % os.getpid()
    sleep(10)
```

在windows cmd中执行：
```
C:\Python\Python2
λ python.exe 002Signal.py
my process ID is 6420
my process ID is 6420
my process ID is 6420
do something                #但按ctl +c 时，调用函数handle_method
```


## Python collections
https://blog.csdn.net/liufang0001/article/details/54618484
### defaultdict() 
#### defaultdict() 与 dict 区别
1. defaultdict()创建字典性能比 dict更高
2. 如果方法字典的value是空时，dict方式创建的字典会抛出KeyError异常的；defaultdict()方式可以利用工厂函数，给初始key带来一个默认值。这个默认值也许是空的list[]  defaultdict(list), 也许是0, defaultdict(int).  
```
mport collections
s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
# defaultdict
d = collections.defaultdict(list)
for k, v in s:
    d[k].append(v)
# Use dict and setdefault   
g = {}
for k, v in s:
    g.setdefault(k, []).append(v)
      
# Use dict
e = {}
for k, v in s:
    e[k] = v
```

## String

### 代码分析： ''.join(result).lstrip('0')[:-k or None] or '0'
此代码分两段''.join(result).lstrip('0')[:-k or None] 和 ’0‘
- ''.join(result).lstrip('0')[:-k or None] 从左到右开始执行：  
- ''.join(result)将字符数组合并成字符串，lstrip('0')然后删除字符串左边所有的字符’0‘，[:-k or None]然后对字符串进行切割。  
- [:-k or None]很重要，执行顺序是：先做判读’-k or None‘，当-k为零时，取None；-k非零时，取值-k。然后再进行切片。[:-k]很简单，大家都知道；[:None]表示不对字符串进行切片，取整个字符串的值。  
- 然后当''.join(result).lstrip('0')[:-k or None]的值为None时，取值’0‘

```  
class Solution(object):
    def removeKdigits(self, num, k):
        result = []
        for d in num:
            while k and result and result[-1] > d:
                result.pop()
                k -= 1
            result.append(d)
        print(''.join(result).lstrip('0'))
        print(''.join(result).lstrip('0')[: -100 or None] or '0')
        print(''.join(result).lstrip('0')[:-k or None] or '0')        
        return ''.join(result).lstrip('0')[:-k or None] or '0'
 
if __name__ == '__main__':    
    num = "1432219"
    num2 = '0001000200'
    k = 1
    Solution().removeKdigits(num, k)  
```

# Python knowlege segments
## Import
如果要引用的脚本与本脚本不在同一个目录级，可以在本脚本开通添加一下代码：
```
import sys
sys.path.append(path)
```
注： path为绝对路径

例如：
```
import sys
sys.path.append('C:/001Work/001Automation/svn/QualityAnalyzer_local1/')
```


## platform
```
local_platform = platform.system()
```

## 正负无穷

Python中可以用如下方式表示正负无穷：
```
float("inf"), float("-inf")
```


## 判读字典key是否为空
### python2  
```
dict.has_key('keyname')
```
### python3 
```
dict.__contains__(chr)              
```                


