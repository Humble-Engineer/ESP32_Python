import ujson
from machine import UART
import time

class JSON_UART:
    
    def __init__(self,num,baud,tx,rx,bits):
        
        self.num     = num
        self.baud    = baud
        self.tx      = tx
        self.rx      = rx
        self.bits    = bits
        
        self.uart = UART(self.num, baudrate=self.baud, tx=self.tx, rx=self.rx, data_bits=self.bits)

        self.sand_data = {"order": "run", "value": 300}
        self.recv_data = ''
        
    # 发送数据
    def send(self,data):
        # 将数据转换为JSON格式
        json_data = ujson.dumps(data)
        # 发送JSON数据
        uart.write(json_data + '\n')

    # 接收数据
    def recv(self,end_char='\n'):
        received_data = b''  # 使用字节串来存储接收到的数据
        while uart.any():
            char = uart.read(1)  # 读取一个字符
            if char == end_char.encode():  # 将结束字符转换为字节串并比较
                try:
                    # 尝试解析JSON数据
                    json_data = ujson.loads(received_data.decode())
                    return json_data
                except Exception as e:
                    print("Error decoding JSON:", e)
                    return None
            elif char:
                received_data += char  # 将字符添加到接收到的数据中
        return None

    # 执行json数据对应的操作
    def execute(self,data):
        if   data['order'] == "run":
            print("run:",data['value'])
        elif data['order'] == "stop":
            print("stop:",data['value'])
        else:
            print("default case")
        
# 配置串口
serial = JSON_UART(num=1,baud=115200,tx=21,rx=19,bits=8)  # 根据硬件配置进行调整

# 发送数据
serial.send(serial.sand_data)
print("Send data:", serial.sand_data)

while 1:
    # 等待一段时间，模拟其他操作
    time.sleep(0.1)
    # 接收数据(读取一个数据包，其余留在串口缓存区)
    serial.recv_data = recv(end_char='}')
    # 处理接收到的数据
    if recv_data != None :
        # 打印接收到的json数据
        print("Recv data:", serial.recv_data)
        # 执行json数据对应的操作
        serial.execute(serial.recv_data)
        