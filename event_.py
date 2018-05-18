#!/usr/bin/python
# -*- coding: utf-8 -*-
# author: liu   time: 2018/5/17
import threading
import time

event = threading.Event()


def light():
    c = 0
    event.set()
    while True:
        if 5 < c < 10:
            print('\033[41;1mred 红灯\033[0m')
            event.clear()
        elif c > 10:
            event.set()
            c = 0
        else:
            print '绿灯'
        time.sleep(1)
        c += 1


def car():
    while True:
        if event.is_set():
            print 'run'
            time.sleep(0.8)
        else:
            print('wait')
            event.wait()
            print 'start'


l = threading.Thread(target=light)
c = threading.Thread(target=car)
l.start()
c.start()