
#交互器接口模块sys的导入
import sys
#回到上级目录
sys.path.append("..")
#在根目录下进入drivers文件夹
sys.path.append('./drivers')

#导入oled.py中的OLED类
from oled import OLED

#配置oled显示器
oled = OLED(scl=22,sda=21,timer=(3,1000),
            
            top='ATP detecter',
            top_site=(15,0),
            
            sub1='Flash times:',
            sub1_site=(16,20),
            
            sub2="Last order:",
            sub2_site=(20,40),
            
            data1="",
            data1_site =(55,30),
            
            data2="",
            data2_site =(40,50))

oled.start()

#如果需要后期修改显示内容，直接修改属性即可
#oled.top_heading='Hello World!'