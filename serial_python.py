#!/usr/bin/python3

from concurrent.futures import thread
import os.path
from pickle import NONE
import sys
import serial
import json
import time
import numpy as np
import array
import utils

savelog = False
logline = 0
file = None
fileName = ""
filter_status = None
add_time_stamp=None

def find_match_str(need_matched_str, data_buf):
    for tmp in need_matched_str:
        data_buf = str(data_buf)
        if data_buf.find(tmp) >= 0:
            return 1
    return 0


if __name__ == "__main__":
    with open("./config.json", 'r') as f:
        data = json.load(f)
        savelog = data['log']['savelog']
        logline = data['log']['logline']
        filter_status = data['filter']['filter_is_open']
        add_time_stamp = data['add_time_stamp']
    if savelog == True:
        loglineTmp = logline

    ser = serial.Serial(data['serial_port'], baudrate=115200)
    while True:
        da = ser.readline().decode("utf-8")
        if add_time_stamp == True:
            time_stamp_str = utils.get_time_stamp()
            tmpStr = time_stamp_str + " " + da
        else:
            tmpStr = da
        if filter_status == True:
            if find_match_str(data['filter'][data['filter']['Filter_field_groups']], da) == 1:
                print(tmpStr, end="")
        else:
            print(tmpStr, end="")

        # if savelog == True:
        #     if loglineTmp == logline:
        #         fileName = time_stamp_str+".log"
        #         print(fileName)
        #     loglineTmp = loglineTmp-1
        #     if loglineTmp <= 0:
        #         loglineTmp = logline

