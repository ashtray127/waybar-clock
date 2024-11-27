#!/usr/bin/python

from datetime import datetime
import json

clocks = [
    "󱑋", # 1
    "󱑌", # 2
    "󱑍", # 3
    "󱑎", # 4
    "󱑏", # 5
    "󱑐", # 6
    "󱑑", # 7
    "󱑒", # 8
    "󱑓", # 9
    "󱑔", # 10
    "󱑕", # 11
    "󱑖", # 12
]

current_time = datetime.now()

current_hour = current_time.strftime("%I")

formatted_time = current_time.strftime("%I:%M")

text =  clocks[int(current_hour)] + " " + formatted_time

data = {
    "text": text,
    "tooltip": "", # TODO: Not sure what to add for this, will probably do later
    "class":current_hour
}

print(json.dumps(data))
