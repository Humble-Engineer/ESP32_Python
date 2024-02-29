import ujson
from machine import UART
import time

# 配置串口
uart = UART(1, baudrate=115200, tx=21, rx=19)  # 根据硬件配置进行调整

# 发送数据
def send_data(data):
    # 将数据转换为JSON格式
    json_data = ujson.dumps(data)
    # 发送JSON数据
    uart.write(json_data + '\n')

# 接收数据
def receive_data(end_char='\n'):
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
def execute(data):
    if   data['order'] == "run":
        print("run:",data['value'])
    elif data['order'] == "stop":
        print("stop:",data['value'])
    else:
        print("default case")


# 示例数据
sample_data = {"order": "run", "value": 300}
# 发送数据
send_data(sample_data)
print("Send data:", sample_data)

while 1:
    # 等待一段时间，模拟其他操作
    time.sleep(0.1)
    # 接收数据(读取一个数据包，其余留在串口缓存区)
    recv_data = receive_data(end_char='}')
    # 处理接收到的数据
    if recv_data != None :
        # 打印接收到的json数据
        print("Recv data:", recv_data)
        # 执行json数据对应的操作
        execute(recv_data)
        