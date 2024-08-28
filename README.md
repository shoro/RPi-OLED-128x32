# Raspberry Pi - OLED 128x32

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
Make sure OLED is Connected (diagram below). This step is if you don’t know the address of your I2C Display

![Wiring Diagram.png](https://github.com/shoro/RPi-OLED-128x32/blob/main/img/Wiring%20Diagram.png)

```
sudo apt-get install i2c-tools
```
```
i2cdetect -y 1
```

### 4. CREATE PYTHON CODE TO RUN DISPLAY:
```
sudo nano oledDisplay.py
```
Copy text below:
```
oled = adafruit_ssd1306.SSD1306_I2C(WIDTH, HEIGHT, i2c, addr=0x3C, reset=oled_reset)
```
