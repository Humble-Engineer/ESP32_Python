#交互器接口模块sys的导入
import sys
#回到上级目录
sys.path.append("..")
#在根目录下进入drivers文件夹
sys.path.append('./drivers')

# 在screen.py模块中导入TjcUart这个类
from screen import TjcUart

#导入时间模块
from time import sleep

#实例化对象（设置使用的串口以及数据帧格式）
tjc_uart = TjcUart(id=2,baudrate=115200,tx=17,rx=16,
           begin='|',end='~',num_pos='#',num_neg='$')

'''
#发送字符串命令,跳转到绘图界面
tjc_uart.send("page draw")

#循环发送绘图所需的点
for j in range(4):
    for i in range(200):
        
        #向绘图控件s0的第1、2个通道分别写入数据
        tjc_uart.send("add s0.id,0,"+str(i))
        #tjc_uart.send("add s0.id,1,"+str(200-i))
        
        sleep(0.02)
        
'''


while 1:

    #接收初始信息
    org_recv = tjc_uart.receive()
    #获取初始信息的解码
    cmd_recv = tjc_uart.decode(org_recv)
    
    #打印解码信息
    if cmd_recv != None:
        print(cmd_recv)

    sleep(2)



