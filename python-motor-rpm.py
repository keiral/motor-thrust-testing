import time #libraries
import serial
import datetime
import threading
import motor_control

speed = 110 #forward
#speed = 85 #reverse

start = time.time()

sensor_back = 0
sensor_back_ADC =0 
sensor_front = 0
sensor_front_ADC = 0
const_front = 57
const_back = 26

motor_string = 'M1F'

motor_running_state = False 
motor_terminate = False

file = open("testfile.csv",'w') 
file.write("Time Since Start, Front, Front ADC, Back, Back ADC, RPM \n")

arduino = serial.Serial(
	port='COM7',
	baudrate=256000,
	#parity=serial.None,
	stopbits=serial.STOPBITS_ONE,
	bytesize=serial.EIGHTBITS
)
#arduino.open()

motor = motor_control.get_motor_instance()
motor_control.set_forward()

print("Serial opened")

motor_running_state = True

motor_control.rev_up(30, speed, 0.1)

for k in range(25):
	i = arduino.readline()
	i = arduino.readline()

time.sleep(1)


arduino.flush()
i = arduino.readline()
print("start loop")
for k in range(1000):
	motor_control.set_speed(speed)

	arduino.reset_input_buffer()
	#first line may be gimped
	arduino.readline()
	i = arduino.readline()
	
	try:
		motor.write(b'RVA\r\n')
		sensor_front = (i[0]-const_front)/2.9348
		sensor_front_ADC = i[0]
		sensor_back = (i[2]-const_back)/2.8563
		sensor_back_ADC = i[2]
		x = motor.readline()
	except:
		print("Something went wrong")
		file.write("Err,Err,Err, Err, Err, Err \n")
		print(i)
	else:
		rpm = (x[2] * 255 + x[1])*60

		if k % 25 == 0:
			print( "Sensor Front: ")
			print (sensor_front)
			print( "Sensor Back: ")
			print (sensor_back)

			print ("RPM: ")
			print(rpm)
		current = time.time()
		elapsed = current - start
		file.write(str(elapsed) + ',')
		file.write(str(sensor_front) + ',')
		file.write(str(sensor_front_ADC) + ',')
		file.write(str(sensor_back) + ',')
		file.write(str(sensor_back_ADC) + ',') 
		file.write(str(rpm) + '\n')
print("Done")
motor.write(b'STP\r\n')
motor.close()
file.close()
exit() 