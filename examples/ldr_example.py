#交互器接口模块sys的导入
import sys
#回到上级目录
sys.path.append("..")
#在根目录下进入drivers文件夹
sys.path.append('./drivers')

#导入ldr.py中的LDR类
from ldr import LDR

from time import sleep

#设置模拟量读取引脚，定时器id和触发间隔（ms）
ldr = LDR(pin=34)

while 1:
    ldr.calculate()
    print(ldr.voltage)
    sleep(1)