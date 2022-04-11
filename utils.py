import time


'''
此文件用作通用文件
'''

# 获取时间戳
def get_time_stamp():
    ct = time.time()
    local_time = time.localtime(ct)
    data_head = time.strftime("[%Y-%m-%d %H:%M:%S", local_time)
    data_secs = (ct - int(ct)) * 1000
    time_stamp = "%s.%03d]" % (data_head, data_secs)
    return time_stamp