# Created by: Sorodoc Vlad
# For Raspberry Pi Desktop Case with OLED Stats Display
# Base on Adafruit CircuitPython & SSD1306 Libraries
# Installation & Setup Instructions - https://www.the-diy-life.com/add-an-oled-stats-display-to-raspberry-pi-os-bullseye/
# PSUTIL INSTALL: python -m pip install psutil
import time
import board
import busio
import digitalio
import psutil as PS

from PIL import Image, ImageDraw, ImageFont
import adafruit_ssd1306

import subprocess

# Define the Reset Pin
oled_reset = digitalio.DigitalInOut(board.D4)

# Display Parameters
WIDTH = 128
HEIGHT = 32

# Display Refresh
LOOPTIME = 1

# Use for I2C.
i2c = board.I2C()
oled = adafruit_ssd1306.SSD1306_I2C(WIDTH, HEIGHT, i2c, addr=0x3C, reset=oled_reset)

# Clear display.
oled.fill(0)
oled.show()

# Create blank image for drawing.
# Make sure to create image with mode '1' for 1-bit color.
image = Image.new("1", (oled.width, oled.height))

# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)

# Draw a white background
draw.rectangle((0, 0, oled.width, oled.height), outline=255, fill=255)

font = ImageFont.truetype('PixelOperator.ttf', 16)
#font = ImageFont.load_default()

while True:

    # Draw a black filled box to clear the image.
    draw.rectangle((0, 0, oled.width, oled.height), outline=0, fill=0)

    # Shell scripts
    temps=PS.sensors_temperatures()
    TEMP= "T:{:.1f}°C".format(round(temps['cpu_thermal'][0].current,1))
    
    CPU = "CPU:{:.1f}%".format(round(PS.cpu_percent(),1))
       
    cmd = "free -m | awk 'NR==2{printf \"%.2f%%\", $3*100/$2 }'"
    MemUsage = subprocess.check_output(cmd, shell = True )
    
    cmd = "df -h | awk '$NF==\"/\"{printf \"%d/%dGB %s\", $3,$2,$5}'"
    Disk = subprocess.check_output(cmd, shell = True )

    cmd = "hostname -I | cut -d\' \' -f1"
    IP = subprocess.check_output(cmd, shell = True )
        
    # Pi Stats Display
    draw.text((0, 0), TEMP , font=font, fill=255)
    draw.text((56, 0), CPU, font=font, fill=255)
    draw.text((0, 16), "M:" + str(MemUsage,'utf-8'), font=font, fill=255)
    draw.text((56, 16), "D:" + str(Disk,'utf-8'), font=font, fill=255)
    draw.text((0, 32), "IP: " + str(IP,'utf-8'), font=font, fill=255)
        
    # Display image
    oled.image(image)
    oled.show()
    time.sleep(LOOPTIME)