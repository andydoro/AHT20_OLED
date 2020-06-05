""" Example for using the AHT20 with CircuitPython and the Adafruit library"""

import time
import board
import busio
import adafruit_ahtx0
#import adafruit_sgp30

# OLED
import displayio
import terminalio
from adafruit_display_text import label
import adafruit_displayio_ssd1306

displayio.release_displays()

i2c = busio.I2C(board.SCL, board.SDA, frequency=100000)

# Create library object using our Bus I2C port
#i2c = busio.I2C(board.SCL, board.SDA)
sensor = adafruit_ahtx0.AHTx0(i2c)

# Create library object on our I2C port
#sgp30 = adafruit_sgp30.Adafruit_SGP30(i2c)

#print("SGP30 serial #", [hex(i) for i in sgp30.serial])

#sgp30.iaq_init()
#sgp30.set_iaq_baseline(0x8973, 0x8AAE)


#OLED

display_bus = displayio.I2CDisplay(i2c, device_address=0x3C)
display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=128, height=32)

# Make the display context
splash = displayio.Group(max_size=8)
display.show(splash)

#bg_sprite = displayio.TileGrid(color_bitmap, pixel_shader=color_palette, x=0, y=0)
#splash.append(bg_sprite)

# Draw a smaller inner rectangle
#inner_bitmap = displayio.Bitmap(118, 24, 1)
#inner_palette = displayio.Palette(1)
#inner_palette[0] = 0x000000  # Black
#inner_sprite = displayio.TileGrid(inner_bitmap, pixel_shader=inner_palette, x=5, y=4)
#splash.append(inner_sprite)

# Draw a label
#text = "Hello World!"
#text_area = label.Label(terminalio.FONT, text=text, color=0xFFFF00, x=28, y=15)
#text_area = label.Label(terminalio.FONT, text=text, color=0xFFFF00, x=28, y=15)
#splash.append(text_area)

text = "hello world"
text_area = label.Label(terminalio.FONT, color=0xFFFF00, x=15, y=0, max_glyphs=200)
splash.append(text_area)

#elapsed_sec = 0

while True:
    text_area.text = "temp: %0.1f C \nhumidity: %0.1f %%" % (sensor.temperature, sensor.relative_humidity)
    #print("\nTemperature: %0.1f C" % sensor.temperature)
    #print("Humidity: %0.1f %%" % sensor.relative_humidity)

    #text_area.text = "eCO2 = %d ppm \nTVOC = %d ppb" % (sgp30.eCO2, sgp30.TVOC)
    print(text_area.text)
    #splash.append(text_area)
    #display.show(text_area)
    time.sleep(1)
    #elapsed_sec += 1
    #if elapsed_sec > 10:
    #    elapsed_sec = 0
    #    print(
    #        "**** Baseline values: eCO2 = 0x%x, TVOC = 0x%x"
    #        % (sgp30.baseline_eCO2, sgp30.baseline_TVOC)
    #    )