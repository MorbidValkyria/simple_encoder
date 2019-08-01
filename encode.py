#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 20 18:19:52 2018

@author: francisco
"""

def dcode(data):
    key = 20
    newdata = ''
    for i in data:
        i=ord(i)
        if i< key:
            i = 256 + (1)
        newdata += chr(i-key)
    return newdata
def ncode(data):
    newdata = ''
    key = 20
    for i in data:
        i = ord(i)
        if i + key >= 256:
            i = i - (256)
        newdata += chr(i+key)
    return newdata

with open('hello.txt') as f:
    read_data = f.read()
    encoded = ncode(read_data)
    print(encoded)
    decoded = dcode(encoded)
    print(decoded)

