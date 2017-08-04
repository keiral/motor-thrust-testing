import csv
import sys
import time 
import serial
import datetime
import threading
from time import sleep
from threading import Thread

#global vars


#motor stuff
def doMotors(dir, speed):
    left_motor = serial.Serial(
	    port='/dev/ttyUSB0',
	    baudrate=9600,
	    #parity=serial.None,
	    stopbits=serial.STOPBITS_ONE,
	    bytesize=serial.EIGHTBITS
    )




    right_motor = serial.Serial(
	    port='/dev/ttyUSB1',
	    baudrate=9600,
	    #parity=serial.None,
	    stopbits=serial.STOPBITS_ONE,
	    bytesize=serial.EIGHTBITS
    )
    print "MOTORS DONE"
    while True:
	    x = dir
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
#function space

def UP():
    return 0

def DOWN():
    return 0

def FORWARD():
    return 0

def REVERSE():
    return 0

def parse_csv():
    pass
    if sys.argv[1] == '2.csv':
        #floats
        f = open(sys.argv[1], 'rt')
        try:
            reader = csv.reader(f)
            for row in reader:
                print row
                print float(row[0]) + float(row[1])
        finally:
            f.close()
    elif sys.argv[1] == '1.csv':
        #static commands
        f = open(sys.argv[1], 'rt')
        try:
            reader = csv.reader(f)
            for row in reader:
                counter(row[0],doMotors(row[1], row[2]))
        finally:
            f.close()

#timer
def counter(time,task):

    t = Thread(target=task)

    t.daemon = True
    t.start()

    snooz = time
    sleep(snooz)

#main
def runMotors(time, dir, speed):
    while True:
        #print "To run program, enter 'continue' as command"
        #print "To close program, enter something that's not 'continue'"
        #x = raw_input("Enter Command\r\n")
        #if x != 'continue':
        #    return 0
        #print "continue with program"
        print '0'


#run space
parse_csv()