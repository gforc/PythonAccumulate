
# OS
包含普遍的操作系统功能，如果你希望你的程序能够与平台无关的话，这个模块是尤为重要的。
#

## os.popen
再操作系统终端输入命令，返回输入命令的‘返回值’给变量，可以通过read()和readline()读出  
```
out = os.popen('/usr/local/bin/dfu-util -l', 'r')
for line in (out.readlines()):
    if 'Utopia' in line :
        print(line)
        utopiaID = pattern.findall(line)[0]
        break
``` 
## os.system
直接在终端输入命令，返回‘返回值’
os.system('/usr/local/bin/dfu-util -E 30 -D aa.zip.dfu‘)

##路径相关
```
os.getcwd()
filePath = os.path.join(os.getcwd(),'aa.zip.dfu')
```


os.system('/usr/local/bin/dfu-util -E 30 -D aa.zip.dfu -S ' + utopiaID)


# SYS
提供了一系列有关Python运行环境的变量和函数。
```
>>> sys.platform
'linux'
>>> sys.exit()
```
