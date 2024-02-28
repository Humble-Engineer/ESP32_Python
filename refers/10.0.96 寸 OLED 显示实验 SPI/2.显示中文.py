'''
该程序作用是使用 SPI / SoftSPI 在 OLED 屏幕上显示中文
在线文档：https://docs.geeksman.com/esp32/MicroPython/13.esp32-micropython-spi-oled.html
'''
from machine import Pin, SoftSPI
from libs.ssd1306 import SSD1306_SPI


# 定义对应的管脚对象
spi = SoftSPI(sck=Pin(18), mosi=Pin(13), miso=Pin(19))

# 创建 OLED 对象
oled = SSD1306_SPI(width=128, height=64, spi=spi, dc=Pin(2),
                   res=Pin(15), cs=Pin(4))

# 清屏
oled.fill(0)

# 定义坐标
x = 30
y = 20

# 汉字字典
character_dict = {
    '极': [0x10,0x13,0x10,0x10,0xFC,0x10,0x30,0x38,0x55,0x55,0x91,0x11,0x12,0x12,0x14,0x11,
          0x00,0xFC,0x84,0x88,0x88,0x90,0x9C,0x84,0x44,0x44,0x28,0x28,0x10,0x28,0x44,0x82],

    '客': [0x02,0x01,0x7F,0x40,0x88,0x0F,0x10,0x2C,0x03,0x1C,0xE0,0x1F,0x10,0x10,0x1F,0x10,
          0x00,0x00,0xFE,0x02,0x04,0xF0,0x20,0x40,0x80,0x70,0x0E,0xF0,0x10,0x10,0xF0,0x10],

    '侠': [0x08,0x08,0x08,0x17,0x10,0x32,0x31,0x50,0x9F,0x10,0x10,0x11,0x11,0x12,0x14,0x18,
          0x40,0x40,0x40,0xFC,0x40,0x48,0x50,0x40,0xFE,0xA0,0xA0,0x10,0x10,0x08,0x04,0x02],#侠2

    '实': [0x02,0x01,0x7F,0x40,0x88,0x04,0x04,0x10,0x08,0x08,0xFF,0x01,0x02,0x04,0x18,0x60,
          0x00,0x00,0xFE,0x02,0x84,0x80,0x80,0x80,0x80,0x80,0xFE,0x40,0x20,0x10,0x08,0x04],#实3

    '验': [0x00,0xF8,0x08,0x48,0x48,0x49,0x4A,0x7C,0x04,0x04,0x1D,0xE4,0x44,0x04,0x2B,0x10,
          0x20,0x20,0x50,0x50,0x88,0x04,0xFA,0x00,0x44,0x24,0x24,0xA8,0x88,0x10,0xFE,0x00],#验4

    '室': [0x02,0x01,0x7F,0x40,0x80,0x3F,0x04,0x08,0x1F,0x01,0x01,0x3F,0x01,0x01,0xFF,0x00,
          0x00,0x00,0xFE,0x02,0x04,0xF8,0x00,0x20,0xF0,0x10,0x00,0xF8,0x00,0x00,0xFE,0x00],#室5
    }


def display_zh_character(character, x, y):
    num_list = character_dict[character]
    
    for i in range(16):
        left = bin(num_list[i]).replace('0b', '')
        right = bin(num_list[i + 16]).replace('0b', '')
        
        # 补 0
        while len(left) < 8:
            left = '0' + left
        
        while len(right) < 8:
            right = '0' + right
        
        num_binary = left+right
        
        for j in range(len(num_binary)):
            oled.pixel(x + j, y + i, int(num_binary[j]))
        
def display_zh(text, x, y):
    for i in range(len(text)):
        display_zh_character(text[i], x + i * 16, y)

display_zh('极客侠实验室', 30, 20)
oled.show()

