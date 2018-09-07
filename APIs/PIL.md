# what is PIL
Pillow是Python里的图像处理库（PIL：Python Image Library），提供了了广泛的文件格式支持，强大的图像处理能力，主要包括图像储存、图像显示、格式转换以及基本的图像处理操作等。

# how to ues
```
import PIL
im = Image.open("E:/photoshop/1.jpg") 
print(im.format, im.size, im.mode) 
('JPEG', (600, 351), 'RGB')
```

# API
## Convert
http://blog.csdn.net/icamera0/article/details/50843172

九种不同模式: 1，L，P，RGB，RGBA，CMYK，YCbCr，I，F;

