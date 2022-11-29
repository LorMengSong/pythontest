from machine import Pin,UART
uart = UART(0,96000)
LedGPIO = 16
led = Pin(LedGPIO,Pin.OUT)
led.value(0)
print("Group 2 ================");
while True:
    if uart.any()>0:
        command = uart.read(1);
        if "1" in command:
            led.value(1)
            print("ON")
        elif "0" in command:
            led.value(0)
            print("OFF")    