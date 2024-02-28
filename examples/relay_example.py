#交互器接口模块sys的导入
import sys
#回到上级目录
sys.path.append("..")
#在根目录下进入drivers文件夹
sys.path.append('./drivers')

#导入relay.py中的RELAY类
from relay import RELAY
from time import sleep

relay_stepper = RELAY(32)

relay_stepper.set("on")
sleep(2)
relay_stepper.set("off")