from rpi_ws281x import PixelStrip

LED_COUNT = 24
LED_PIN = 18
LED_FREQ_HZ = 800000
LED_DMA = 10
LED_BRIGHTNESS = 255
LED_INVERT = False
LED_CHANNEL = 0


def init():
    strip = PixelStrip(
        LED_COUNT, 
        LED_PIN, 
        LED_FREQ_HZ, 
        LED_DMA,
        LED_INVERT,
        LED_BRIGHTNESS,
        LED_CHANNEL
    )
    
    strip.begin()
    
    return strip
    
