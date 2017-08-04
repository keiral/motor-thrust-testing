import time
import serial

speed = 128

# configure the serial connections (the parameters differs on the device you are connecting to)
ser = serial.Serial(
    port='COM7',
    baudrate=256000,
    #parity=serial.None,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS
)

ser.isOpen()

for i in range(20):
	time.sleep(1)
	x = ser.readline()
	print(str(x[0]))
#ser.write(b'STP\r\n')
ser.close()