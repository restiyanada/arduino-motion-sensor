import serial
import numpy
import matplotlib.pyplot as plt
from drawnow import *

motions = []
arduinoData = serial.Serial('COM4', 9600) 
plt.ion()
cnt=0

def makeFig(): # function that make our desired plot
        plt.ylim(100,900)
        plt.title('Live Streaming Motion Sensor')
        plt.grid(True)
        plt.ylabel('motion')
        plt.plot(motions, 'ro-', label='Motions')
        plt.legend(loc='upper left')

while True: # while loop that loops forever
        while (arduinoData.inWaiting()==0): # wait here until there is data
                pass #do nothing
        arduinoString = arduinoData.readline() #read line
        motion = float( arduinoString)
        print motion
        motions.append(motion)
        drawnow(makeFig)
        plt.pause(.000001)
        cnt=cnt+1
        if(cnt>50):
                motions.pop(0)
