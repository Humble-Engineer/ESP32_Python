#交互器接口模块sys的导入
import sys
#回到上级目录
sys.path.append("..")
#在根目录下进入drivers文件夹
sys.path.append('./drivers')

#导入motor.py中的MOTOR类
from motor import MOTOR
from time import sleep

#实例化一个电机对象（注意速度引脚PWM占用的定时器id）
motor = MOTOR(spd=33,ena=25,dir=26)

#顺时针旋转，设置转速
motor.clockwise()
motor.speed(600)
sleep(5)

#逆时针旋转，设置转速
motor.anticlockwise()
motor.speed(1980)
sleep(5)

#急停、启动、急停
motor.stop()
sleep(1)
motor.run()
sleep(3)
motor.stop()
sleep(1)