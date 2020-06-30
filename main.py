﻿#!/usr/bin/python
# -*- coding:utf-8 -*-

import time
import config
import traceback
import datetime
import os
import asyncio
import json
import aiohttp
from pihole import PiHole
import SH1106
from PIL import Image,ImageDraw,ImageFont


try:
    disp = SH1106.SH1106()
    print("\r\1.3inch OLED")
    # Initialize library.
    disp.Init()
    # Clear display.
    while True:
        print("updating")
        disp.clear()
        # Create blank image for drawing.
        image1 = Image.new('1', (disp.width, disp.height), "WHITE")
        draw = ImageDraw.Draw(image1)
        print("loading fonts")
        font_file = os.path.join(os.path.dirname(__file__), "Font.ttf")
        font = ImageFont.truetype(font_file, 18)
        font10 = ImageFont.truetype(font_file,16)
        draw.line([(0,0),(127,0)], fill = 0)
        draw.line([(0,0),(0,63)], fill = 0)
        draw.line([(0,63),(127,63)], fill = 0)
        draw.line([(127,0),(127,63)], fill = 0)
        draw.text((10,0), datetime.datetime.now().strftime("%H:%M"), font = font10, fill = 0)
        draw.text((10,20), datetime.datetime.now().strftime("%b %-d, %a"), font = font, fill = 0)
        # image1=image1.rotate(180) 
        disp.ShowImage(disp.getbuffer(image1))
        time.sleep(60)
    #print ("***draw image")
    #Himage2 = Image.new('1', (disp.width, disp.height), 255)  # 255: clear the frame
    #bmp = Image.open('pic.bmp')
    #Himage2.paste(bmp, (0,5))
    # Himage2=Himage2.rotate(180) 	
    #disp.ShowImage(disp.getbuffer(Himage2))
except IOError as e:
    print(e)
except KeyboardInterrupt:    
    print("ctrl + c:")
    epdconfig.module_exit()
    exit()
