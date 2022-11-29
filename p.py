import serial #import Library Serial
import time #define time to process
from tkinter import* #import library to create GUI

ArduinoSerial = serial.Serial('COM1',9600,timeout=1)#convert serial port ardunio to python process GUI controll led
time.sleep(2)#waite for 2s to process

status1=0#define varuible 

def led_on(): #set function led_on to process when click button on led "HIGH"
    ArduinoSerial.write(b'1') #send byte '1' to byte deconde
def led_off(): #set function led_on to process when click button on led "LOW"
    ArduinoSerial.write(b'0') #send byte '0' to byte deconde
def led_Exit():
    ArduinoSerial.write(b'0')
    status1="Quit"
    quit()
root=Tk() #process on GUI
root.title("Ardunio Butoon On and OFF LED")#set title of GUI
ms=Label(root, text="Create By Keo Visal",font=("Consoles",15))
btn1=Button(root, text="led on",command=led_on)
btn2=Button(root, text="led off",command=led_off)
btn3=Button(root, text="Exit",command=led_Exit)

ms.pack()
btn1.pack()
btn2.pack()
btn3.pack()

root.geometry('1000*1000')
root.mainloop()