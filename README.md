# Raspberry Pi - OLED 128x32

Links:

[CASE](https://www.prusaprinters.org/prints/106225-modular-snap-together-raspberry-pi-2b3b3b4-case-w-)

### 1. ENABLE I2C

```
sudo raspi-config
```
3 Interface Option -> I4 SPI -> Yes <br>
3 Interface Option -> I5 I2C -> Yes

### 2. INSTALL NECESSARY FILES
```
sudo apt update
```
```
sudo apt upgrade -y
```
```
sudo apt-get install python3-pip
```
May or May not be needed:
```
sudo pip3 install --upgrade setuptools
```
```
pip3 install adafruit-circuitpython-ssd1306
```
```
sudo apt-get install python3-pip
```
```
sudo apt-get install python3-pil
```
For showing Temperature:
```
sudo pip3 install gpiozero
```
```
sudo pip3 install adafruit-circuitpython-ssd1306
```
```
sudo pip3 install adafruit-blinka
```

### 3. GET OLED ADDRESS
Make sure OLED is Connected <em><b>(diagram below)</b></em>. This step is if you don’t know the address of your I2C Display

![Wiring Diagram.png](https://github.com/shoro/RPi-OLED-128x32/blob/main/img/Wiring%20Diagram.png)

```
sudo apt-get install i2c-tools
```
```
i2cdetect -y 1
```
Example:
<em>(You should see something like this)</em>

![OLED I2C Address.png](https://github.com/shoro/RPi-OLED-128x32/blob/main/img/OLED%20I2C%20Address.png)

### 4. CREATE PYTHON CODE TO RUN DISPLAY:
```
sudo nano oledDisplay.py
```
Copy text below:<br>
(We need to update the OLED address <b>0x3C</b> to the one from the i2cdetect -y 1 step above.)
```
oled = adafruit_ssd1306.SSD1306_I2C(WIDTH, HEIGHT, i2c, addr=0x3C, reset=oled_reset)
```
When everything is updated save and close: <em>CTRL+X -> Y -> ENTER</em>

### 5. RUN PYTHON DISPLAY FILE
```
python oledDisplay.py
```

### 6. ADD TO STARTUP
If you want this to automatically startup with your Pi
```
sudo nano /etc/rc.local
```
Go to very end right before exit 0 and add:
```
echo "Starting OLED Display..."
/usr/bin/python3 /home/pi/oledDisplay.py
```
Save and close: <em>CTRL+X -> Y -> ENTER</em>

Change Permissions:
```
sudo chmod a+x oledDisplay.py
```
