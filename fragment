



# Import
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

# os
```
PWD = os.getcwd()
```
# platform
```
local_platform = platform.system()
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


# 正负无穷

Python中可以用如下方式表示正负无穷：
```
float("inf"), float("-inf")
```
