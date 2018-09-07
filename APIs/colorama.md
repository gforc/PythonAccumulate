# what is colorama
colorama是一个python专门用来在控制台、命令行输出彩色文字的模块，可以跨平台使用。
# install

pip3 install colorama
　　
# format

```
Fore: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
Back: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
Style: DIM, NORMAL, BRIGHT, RESET_ALL
```
 

# some example 

```
from colorama import Fore,Back,Style
print (Fore.RED + "some red text")
print (Back.GREEN + "and with a green background")
print (Style.DIM + "and in dim text")
print (Style.RESET_ALL)
print ("back to normal now!!")
```
 
