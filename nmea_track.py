#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 15 15:03:07 2020

@author: daryamalafeeva
"""

import codecs
import math
import ddmm2rad

line_list      = []
lattitude_list = []
longitude_list = []
height_list    = []

with codecs.open("/Users/daryamalafeeva/Desktop/SN_6703/rgfile_20191008_122907.txt", "r",encoding='utf-8', errors='ignore') as NMEA_log:
    for line in NMEA_log:
        if line.startswith('$GNGGA'):
            str_massive     = line.split(',')
            get_latitude    = float(str_massive[2])
            get_longitude   = float(str_massive[4])
            get_height      = float(str_massive[9])
            # преобразуем формат ddmm в радианны
            lat = ddmm2rad.func(get_latitude)
            lon = ddmm2rad.func(get_longitude)
            
#            get_latitude_ns = str_massive[3]
#            if get_latitude_ns == 'N':
            lattitude_list.append(lat)
 #           elif get_latitude_ns == 'S':
            longitude_list.append(lon)
            height_list.append(get_height)
                


# построение трека НМ






