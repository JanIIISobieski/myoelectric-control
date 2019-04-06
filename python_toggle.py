#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  6 09:47:39 2019

@author: gabriel
"""

from arduino_communication import Arduino

arduino = Arduino()

val_to_send = 0

while True:

    x = input()
    arduino.send_through_serial((val_to_send % 2 + 1))
    arduino.wait_for_response()
    val_to_send += 1
