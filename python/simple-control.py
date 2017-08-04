import time #libraries
import serial
import datetime
import threading



speed = 100



left_motor = serial.Serial(
	port='/dev/ttyUSB0',
	baudrate=9600,
	#parity=serial.None,
	stopbits=serial.STOPBITS_ONE,
	bytesize=serial.EIGHTBITS
)
#arduino.open()



right_motor = serial.Serial(
	port='/dev/ttyUSB1',
	baudrate=9600,
	#parity=serial.None,
	stopbits=serial.STOPBITS_ONE,
	bytesize=serial.EIGHTBITS
)



while True:
	x = input("Enter Command\r\n")
	string = "STP\r\n"
	left_motor.write(string.encode())
	right_motor.write(string.encode())
	
	if x == "UP":
		string = "M3F" + chr(speed) + "\r\n"
		left_motor.write(string.encode())
		right_motor.write(string.encode())
	if x == "DOWN":
		string = "M3R" + chr(speed) + "\r\n"
		left_motor.write(string.encode())
		right_motor.write(string.encode())
	if x == "FORWARD":
		string = "M1F" + chr(speed) + "\r\n"
		left_motor.write(string.encode())
		right_motor.write(string.encode())
		string = "M2F" + chr(speed) + "\r\n"
		left_motor.write(string.encode())
		right_motor.write(string.encode())
	if x == "REVERSE":
		string = "M1R" + chr(speed) + "\r\n"
		left_motor.write(string.encode())
		right_motor.write(string.encode())
		string = "M2R" + chr(speed) + "\r\n"
		left_motor.write(string.encode())
		right_motor.write(string.encode())