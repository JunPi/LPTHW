## 安装方法
我查阅了两种安装方式：
- 官网下载PKG文件安装（www.python.org）
- Homebrew 下用LC装 （refer to [The hitchhiker's guider to python](http://docs.python-guide.org/en/latest/))
我采用了第二种方法。

## 问题
目前尚未symlink上Python3。
自己参考The hitchhiker's guider to python 在.bash_profile里增加PATH，如下:  
export PATH=/usr/local/bin:/usr/local/sbin:~/bin:$PATH  
折腾了一段时间及时止损了，目前默认interpretor(解释器）为系统自带的Python 2,执行Python 3 程序
需要加上python3, 例如 $ python3 ex1.py。

