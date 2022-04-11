#!/usr/bin/python3

from concurrent.futures import thread
import os.path
import sys
import serial
import json
import time
import numpy as np
import array
import utils

savelog=False
logline=0
file=None
fileName=""

def find_match_str(need_matched_str,data_buf):
    for tmp in need_matched_str:
        data_buf = str(data_buf)
        if data_buf.find(tmp) >= 0:
            return 1
    return 0

if __name__ == "__main__":
    with open("./config.json",'r') as f:
        data = json.load(f)
        savelog=data['savelog']
        logline=data['logline']
    if savelog == True:
            loglineTmp = logline
    ser = serial.Serial(data['serial_port'],baudrate=115200)
    while True:
        da = ser.readline().decode("utf-8")
        if find_match_str(data['filter_key_words'],da) == 1:
            time_stamp_str=utils.get_time_stamp()
            tmpStr = time_stamp_str + " " + da
            print(tmpStr,end="")
            if savelog == True:
                if loglineTmp == logline:
                    fileName = time_stamp_str+".log"
                    print(fileName)
                loglineTmp=loglineTmp-1
                if loglineTmp <= 0:
                    loglineTmp = logline



                



