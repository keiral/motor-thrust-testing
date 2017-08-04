import serial, time

motor_string = 'M1F'

motor = serial.Serial(
	port='COM8',
	baudrate=9600,
	#parity=serial.None,
	stopbits=serial.STOPBITS_ONE,
	bytesize=serial.EIGHTBITS
)

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
		
def set_speed(speed):
	print("string out: " + message + " speed is: " + str(speed))
	motor.write(message.encode())