## This is course material for Introduction to Python Scientific Programming
## Example code: matplotlib_clock.py
## Author: Allen Y. Yang
##
## (c) Copyright 2020. Intelligent Racing Inc. Not permitted for commercial use

from datetime import datetime
import matplotlib.pyplot as plt
import os
import numpy as np

# Initialization, define some constant
path = os.path.dirname(os.path.abspath(__file__))
filename = path + '/airplane.bmp'
background = plt.imread(filename)

second_hand_length = 200
second_hand_width = 2
minute_hand_length = 150
minute_hand_width = 6
hour_hand_length = 100
hour_hand_width = 10

center = np.array([256, 256])
def clock_hand_vector(angle, length):
    return np.array([length * np.sin(angle), -length * np.cos(angle)])

# draw an image background
fig, ax = plt.subplots()
ax.set_axis_off()
while True:
    plt.imshow(background)

    # First retrieve the time
    now_time = datetime.now()
    hour = now_time.hour
    if hour>12: hour = hour - 12
    minute = now_time.minute
    second = now_time.second

    # Calculate end points of hour, minute, second
    rps = second/60*2*np.pi
    rpm = (minute + second / 60) / 60 * 2 * np.pi
    rph = (hour + minute / 60 + second / 3600) / 12 * 2 * np.pi
    rpgmth = hour + 7/ 24 * 2 * np.pi
    hour_vector = clock_hand_vector(rph, hour_hand_length)
    minute_vector = clock_hand_vector(rpm, minute_hand_length)
    second_vector = clock_hand_vector(rps, second_hand_length)
    gmt_vector = clock_hand_vector(rpgmth, second_hand_length)
    
    plt.arrow(center[0], center[1], hour_vector[0], hour_vector[1], head_length = 3, linewidth = hour_hand_width, color = 'black')
    plt.arrow(center[0], center[1], gmt_vector[0], gmt_vector[1], head_length = 3, linewidth = hour_hand_width, color = 'yellow')
    plt.arrow(center[0], center[1], minute_vector[0], minute_vector[1], linewidth = minute_hand_width, color = 'black')
    plt.arrow(center[0], center[1], second_vector[0], second_vector[1], linewidth = second_hand_width, color = 'red')

    plt.pause(0.01)
    plt.clf()
