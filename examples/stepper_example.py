#交互器接口模块sys的导入
import sys
#回到上级目录
sys.path.append("..")
#在根目录下进入drivers文件夹
sys.path.append('./drivers')

#导入stepper.py中的STEPPER类
from stepper import STEPPER
from time import sleep,sleep_ms,sleep_us

#实例化一个步进电机对象
stepper = STEPPER(ena=4,dir=2,pul=15)

for i in range(1):
    
    #以300rmp的速度按逆时针方向旋转10圈
    stepper.location(rol=11,spd=260,dir="anticlock")
    sleep(2)

    #以300rmp的速度按顺时针方向旋转10圈
    stepper.location(rol=11,spd=260,dir="clockwise")
    sleep(2)

'''
#以300rmp的速度按逆时针方向旋转，保持2秒
stepper.speed_rmp(spd=300,dir="anticlock")
sleep(2)
print("第3条命令完成！")

#以300rmp的速度按顺时针方向旋转，保持2秒
stepper.speed_rmp(spd=300,dir="clockwise")
sleep(2)
print("第4条命令完成！")

stepper.stop()
'''