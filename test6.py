import serial
import time
ArduinoSerial = serial.Serial("com4",9600);
time.sleep(2)
print("Enter 1 to run ON LED and 0 to turn OFF LED");
while 1:
    var = input()
    print("you entered".var);
    if(var == '1'):
        ArduinoSerial.write(b,'1');
        print("LED turned ON");
        time.sleep(1)
    elif(var == '0'):
        ArduinoSerial.write(b,'0')    