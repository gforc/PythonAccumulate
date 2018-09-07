
在liunx系统中要想每隔一分钟执行一个命令，最普遍的方法就是crontab了，如果不想使用crontab，经同事指点在程序中可以用定时器实现这种功能，于是就开始摸索了，发现需要一些信号的知识...
查看你的linux支持哪些信号：kill -l 即可

root@server:~# kill -l
 1) SIGHUP   2) SIGINT   3) SIGQUIT  4) SIGILL   5) SIGTRAP
 6) SIGABRT  7) SIGBUS   8) SIGFPE   9) SIGKILL 10) SIGUSR1
11) SIGSEGV 12) SIGUSR2 13) SIGPIPE 14) SIGALRM 15) SIGTERM
16) SIGSTKFLT   17) SIGCHLD 18) SIGCONT 19) SIGSTOP 20) SIGTSTP
21) SIGTTIN 22) SIGTTOU 23) SIGURG  24) SIGXCPU 25) SIGXFSZ
26) SIGVTALRM   27) SIGPROF 28) SIGWINCH    29) SIGIO   30) SIGPWR
31) SIGSYS  34) SIGRTMIN    35) SIGRTMIN+1  36) SIGRTMIN+2  37) SIGRTMIN+3
38) SIGRTMIN+4   39) SIGRTMIN+5 40) SIGRTMIN+6 41) SIGRTMIN+7 42) SIGRTMIN+8
43) SIGRTMIN+9   44) SIGRTMIN+10 45) SIGRTMIN+11 46) SIGRTMIN+12    47) SIGRTMIN+13
48) SIGRTMIN+14 49) SIGRTMIN+15 50) SIGRTMAX-14 51) SIGRTMAX-13 52) SIGRTMAX-12
53) SIGRTMAX-11 54) SIGRTMAX-10 55) SIGRTMAX-9  56) SIGRTMAX-8 57) SIGRTMAX-7
58) SIGRTMAX-6   59) SIGRTMAX-5 60) SIGRTMAX-4 61) SIGRTMAX-3 62) SIGRTMAX-2
63) SIGRTMAX-1 64) SIGRTMAX 
root@server:~#


# 信号

    信号：进程之间通讯的方式，是一种软件中断。一个进程一旦接收到信号就会打断原来的程序执行流程来处理信号。操作系统规定了进程收到信号以后的默认行为，但是，我们可以通过绑定信号处理函数来修改进程收到信号以后的行为，有两个信号是不可更改的SIGTOP和SIGKILL。 
发送信号一般有两种原因:
    1(被动式)  内核检测到一个系统事件.例如子进程退出会像父进程发送SIGCHLD信号.键盘按下control+c会发送SIGINT信号
    2(主动式)  通过系统调用kill来向指定进程发送信号

   在C语言中有个setitimer函数，函数setitimer可以提供三种定时器，它们相互独立，任意一个定时完成都将发送定时信号到进程，并且自动重新计时。参数which确定了定时器的类型：

ITIMER_REAL       定时真实时间，与alarm类型相同。              SIGALRM
ITIMER_VIRT       定时进程在用户态下的实际执行时间。            SIGVTALRM
ITIMER_PROF       定时进程在用户态和核心态下的实际执行时间。      SIGPROF
  这三种定时器定时完成时给进程发送的信号各不相同，其中ITIMER_REAL类定时器发送SIGALRM信号，ITIMER_VIRT类定时器发送SIGVTALRM信号，ITIMER_REAL类定时器发送SIGPROF信号。
  函数alarm本质上设置的是低精确、非重载的ITIMER_REAL类定时器，它只能精确到秒，并且每次设置只能产生一次定时。函数setitimer设置的定时器则不同，它们不但可以计时到微妙（理论上），还能自动循环定时。在一个Unix进程中，不能同时使用alarm和ITIMER_REAL类定时器。

    SIGINT    终止进程     中断进程  (control+c)
    SIGTERM   终止进程     软件终止信号
    SIGKILL   终止进程     杀死进程
    SIGALRM   闹钟信号

前期的知识也准备的差不多了，该向python的signal进军了。

定义信号名

signal包定义了各个信号名及其对应的整数，比如

```
import signal
print signal.SIGALRM
print signal.SIGCONT
Python所用的信号名和Linux一致。你可以通过
```

```
$man 7 signal
```

# 查询

预设信号处理函数

signal包的核心是使用signal.signal()函数来预设(register)信号处理函数，如下所示：

singnal.signal(signalnum, handler)
signalnum为某个信号，handler为该信号的处理函数。我们在信号基础里提到，进程可以无视信号，可以采取默认操作，还可以自定义操作。当handler为signal.SIG_IGN时，信号被无视(ignore)。当handler为singal.SIG_DFL，进程采取默认操作(default)。当handler为一个函数名时，进程采取函数中定义的操作。
```
import signal
# Define signal handler function
def myHandler(signum, frame):
  print('I received: ', signum)
 
# register signal.SIGTSTP's handler 
signal.signal(signal.SIGTSTP, myHandler)
signal.pause()
print('End of Signal Demo')
 ```

在主程序中，我们首先使用signal.signal()函数来预设信号处理函数。然后我们执行signal.pause()来让该进程暂停以等待信号，以等待信号。当信号SIGUSR1被传递给该进程时，进程从暂停中恢复，并根据预设，执行SIGTSTP的信号处理函数myHandler()。myHandler的两个参数一个用来识别信号(signum)，另一个用来获得信号发生时，进程栈的状况(stack frame)。这两个参数都是由signal.singnal()函数来传递的。
上面的程序可以保存在一个文件中(比如test.py)。我们使用如下方法运行:


$python test.py
以便让进程运行。当程序运行到signal.pause()的时候，进程暂停并等待信号。此时，通过按下CTRL+Z向该进程发送SIGTSTP信号。我们可以看到，进程执行了myHandle()函数, 随后返回主程序，继续执行。(当然，也可以用$ps查询process ID, 再使用$kill来发出信号。)(进程并不一定要使用signal.pause()暂停以等待信号，它也可以在进行工作中接受信号，比如将上面的signal.pause()改为一个需要长时间工作的循环。)

我们可以根据自己的需要更改myHandler()中的操作，以针对不同的信号实现个性化的处理。

# 定时发出SIGALRM信号

一个有用的函数是signal.alarm()，它被用于在一定时间之后，向进程自身发送SIGALRM信号:

```
import signal
# Define signal handler function
def myHandler(signum, frame):
  print("Now, it's the time")
  exit()
 
# register signal.SIGALRM's handler 
signal.signal(signal.SIGALRM, myHandler)
signal.alarm(5)
while True:
  print('not yet')
```
我们这里用了一个无限循环以便让进程持续运行。在signal.alarm()执行5秒之后，进程将向自己发出SIGALRM信号，随后，信号处理函数myHandler开始执行。 

# 发送信号

signal包的核心是设置信号处理函数。除了signal.alarm()向自身发送信号之外，并没有其他发送信号的功能。但在os包中，有类似于linux的kill命令的函数，分别为

```
os.kill(pid, sid)
os.killpg(pgid, sid)
```
分别向进程和进程组(见Linux进程关系)发送信号。sid为信号所对应的整数或者singal.SIG*。

实际上signal, pause，kill和alarm都是Linux应用编程中常见的C库函数，在这里，我们只不过是用Python语言来实现了一下。实际上，Python 的解释器是使用C语言来编写的，所以有此相似性也并不意外。此外，在Python 3.4中，signal包被增强，信号阻塞等功能被加入到该包中。我们暂时不深入到该包中。
