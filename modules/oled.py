
from machine import Pin, SoftI2C, I2C, Timer


# 导入驱动库（ssd1306）
from modules.drivers.ssd1306 import SSD1306_I2C

class OLED:
    
    def __init__(self,sda,scl,timer,
                 top,top_site,
                 sub1,sub1_site,
                 sub2,sub2_site,
                 data1,data1_site,
                 data2,data2_site):
        
        #iic总线连接的单片机引脚
        self.scl = scl
        self.sda = sda
        
        #如果是硬件所在引脚，直接构造硬件iic总线
        if scl==18 and sda==19:
            self.i2c = I2C(0)
            
        elif scl==25 and sda==26:
            self.i2c = I2C(1)
        
        else :
            #生成模拟iic总线
            self.i2c = SoftI2C(sda=Pin(sda),scl=Pin(scl))
        
        
        #oled构造函数
        self.oled = SSD1306_I2C(128,64,self.i2c,addr=0x3c)
        
        #oled屏幕刷新定时器id和周期（单位：ms）
        self.timer_id = timer[0]
        self.timer_period = timer[1]
        
        #需要显示的总标题、子标题1和子标题2
        self.top_heading  = top
        self.sub_heading1 = sub1
        self.sub_heading2 = sub2
        
        #需要显示的两个数据
        self.data1 = data1
        self.data2 = data2
        
        #各个显示部分的位置（x,y）（单位：像素点）
        self.top_site   = top_site
        self.sub1_site  = sub1_site
        self.sub2_site  = sub2_site
        self.data1_site = data1_site
        self.data2_site = data2_site
        
        self.flash_time = 0
        
        print("OLED初始化完成！",end='\n')
        
    # 指定位置显示内容
    def display(self,string,x,y):
        self.oled.text(string,x,y)
        self.oled.show()

    # 清除屏幕显示
    def clear(self):
        self.oled.fill(0)
        
    # 屏幕显示
    def show(self):
        
        self.clear()
        
        #转换为字符串
        data1 = str(self.data1)
        data2 = str(self.data2)

        # 显示到特定位置
        self.display(self.top_heading,
                     self.top_site[0],
                     self.top_site[1])
        
        self.display(self.sub_heading1,
                     self.sub1_site[0],
                     self.sub1_site[1])
        
        self.display(self.sub_heading2,
                     self.sub2_site[0],
                     self.sub2_site[1])

        self.display(data1,
                     self.data1_site[0],
                     self.data1_site[1])
        
        self.display(data2,
                     self.data2_site[0],
                     self.data2_site[1],)

    # 回调函数
    def fun(self,tim):
        
        self.flash_time += 1
        self.data1=self.flash_time
        
        self.show()

    # 启用定时器
    def start(self):
        
        tim = Timer(self.timer_id)
        tim.init(period=self.timer_period,mode=Timer.PERIODIC,callback=self.fun)
        
        self.show()

    # 禁用定时器
    def stop(self):
        
        self.show()
        
        tim = Timer(self.timer_id)
        tim.deinit()
        
if __name__ == "__main__":
    
    import os

    current_path = os.getcwd()
    print("Current working directory:", current_path)


    #配置oled显示器
    oled = OLED(scl=18,sda=19,timer=(3,1000),
                
                top='moniter',
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





