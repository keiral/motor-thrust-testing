import serial
import time
import motor_control

#speed = 100
max_speed = 110 #120 & 110 & 100 had no problems with simple testing in forward and reverse
motor_string = 'M1R'
lowest_speed = 27*2 #best value = 27

"""
message = 'M1F'+chr(speed)+'\r\n'
print("string out: " + message + " speed is: " + str(speed))
motor.write(message.encode())
time.sleep(3)
"""
"""
for count in range(10):
	motor_control.rev_up(lowest_speed, max_speed, 0.1)
	motor_control.rev_down(max_speed, lowest_speed, 0.1)
	print("Count is: " + str(count + 1))
	for num in range(20):
		print(count + 1)
"""

motor_control.rev_up(lowest_speed, max_speed, 0.1)
for i in range(10):
	motor_control.set_speed(max_speed)
	time.sleep(2)

motor_control.stop()
