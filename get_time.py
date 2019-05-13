#This code get time use pc

import time

def get_time():
    time.localtime(time.time())
    now_time = time.strftime('%Y-%m-%d',time.localtime(time.time()))
    return now_time
