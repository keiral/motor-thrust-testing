import serial
import time

#speed = 100
max_speed = 85 #120 & 110 & 100 had no problems with simple testing in forward and reverse
motor_string = 'M1R'
lowest_speed = 27 #best value = 27

motor = serial.Serial(
	port='COM8',
	baudrate=9600,
	#parity=serial.None,
	stopbits=serial.STOPBITS_ONE,
	bytesize=serial.EIGHTBITS
)

"""
message = 'M1F'+chr(speed)+'\r\n'
print("string out: " + message + " speed is: " + str(speed))
motor.write(message.encode())
time.sleep(3)
"""

def rev_down(max, min, delay):
	for i in range(max, min, -1):
		speed = i
		message = motor_string+chr(speed)+'\r\n'
		print("string out: " + message + " speed is: " + str(speed))
		motor.write(message.encode())
		time.sleep(delay)

def rev_up(min, max, delay):
	for i in range(min, max):
		speed = i
		message = motor_string+chr(speed)+'\r\n'
		print("string out: " + message + " speed is: " + str(speed))
		motor.write(message.encode())
		time.sleep(delay)

for count in range(10):
	rev_up(lowest_speed, max_speed-5, 0.2)
	rev_up(max_speed-5, max_speed, 2)
	rev_down(max_speed, max_speed-10, 0.2)
	rev_down(max_speed-10, lowest_speed, 0.2)
	print("Count is: " + str(count + 1))
	for num in range(20):
		print(count + 1)

motor.write("STP\r\n".encode())