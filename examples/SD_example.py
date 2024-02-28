#交互器接口模块sys的导入
import sys
#回到上级目录
sys.path.append("..")
#在根目录下进入drivers文件夹
sys.path.append('./drivers')

#导入sd.py中的SD类
from sd import SD

#初始化sd卡的SPI总线
sd = SD(miso=13,mosi=12,sck=14,cs=27)
#查看sd卡中根目录下的文件
sd.view()

#向'文件名'写入'内容'，没有此文件名会自动生成
sd.write('test0.txt','hello world!')
sd.write('test1.txt',str(114514))
sd.write('test2.txt',str(3.14159))
