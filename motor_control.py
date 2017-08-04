import serial, time

motor_string = 'M1F'

motor = serial.Serial(
	port='COM8',
	baudrate=9600,
	#parity=serial.None,
	stopbits=serial.STOPBITS_ONE,
	bytesize=serial.EIGHTBITS
)

def get_motor_instance():
	return motor

def set_forward():
	global motor_string
	motor_string = 'M1F'

def set_reverse():
	global motor_string
	motor_string = 'M1R'

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
		
def set_speed(speed, do_print = False):
	message = motor_string+chr(speed)+'\r\n'
	if do_print:
		print("string out: " + message + " speed is: " + str(speed))
	motor.write(message.encode())
	
def stop():
	motor.write(b'STP\r\n')

def close():
	motor.close()