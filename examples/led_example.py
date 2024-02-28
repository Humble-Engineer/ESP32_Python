#交互器接口模块sys的导入
import sys
#回到上级目录
sys.path.append("..")
#在根目录下进入drivers文件夹
sys.path.append('./drivers')

#导入led.py中的LED类
from led import LED

# 将led作为LED类的实例化对象，引脚为2号
led = LED(2)

# 调用LED类中的blink方法，时间间隔为1秒
while 1:
    led.blink(0.5)

