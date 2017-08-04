import serial, time

const_star = 26
const_port = 57

arduino = serial.Serial(
	port='COM7',
	baudrate=256000,
	#parity=serial.None,
	stopbits=serial.STOPBITS_ONE,
	bytesize=serial.EIGHTBITS
)

arduino.flush()
i = arduino.readline()

for i in range(100):
	arduino.reset_input_buffer()
	i = arduino.readline()
	sensor_starboard = (i[0]-const_star)/2.9348
	sensor_starboard_ADC = i[0]
	sensor_port = (i[2]-const_port)/2.8563
	sensor_port_ADC = i[2]
	print("Sensor Starboard: ")
	print(sensor_starboard_ADC)
	print("Sensor Port: ")
	print(sensor_port_ADC)
	time.sleep(1)