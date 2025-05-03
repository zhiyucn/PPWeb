import time
import datetime

def time_command(colur="black"):
    
    # 获取当前时间
    now = datetime.datetime.now()
    # 格式化时间为字符串
    time_str = now.strftime("%Y-%m-%d %H:%M:%S")
    return time_str
