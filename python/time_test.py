import csv
import sys
from time import sleep
import serial
import datetime
from threading import Thread
import time
import threading


def task():
    while True:
        pass



def counter(time):

    t = Thread(target=task)

    t.daemon = True
    t.start()

    snooz = time
    sleep(snooz)

counter(4)
