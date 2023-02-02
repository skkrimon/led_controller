from rpi_ws281x import Color


def static(strip, r, g, b, delay_ms=50):
    print('test from function')
    #for i in range(strip.numPixels()):
    #    strip.setPixelColor(i, Color(r, g, b))
    #    strip.show(delay_ms / 1000.0)
        
        
def clear(strip):
    static(strip, 0, 0, 0)
        