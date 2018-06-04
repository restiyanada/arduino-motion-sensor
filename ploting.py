import serial
import numpy
import matplotlib.pyplot as plt
from drawnow import *

arduinoData = serial.Serial('COM4', 9600) 

while True: # while loop that loops forever
	while (arduinoData.inWaiting()==0): # wait here until there is data
		pass #do nothing
	arduinoString = arduinoData.readline()
	print arduinoString