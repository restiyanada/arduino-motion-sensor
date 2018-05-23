import serial
import MySQLdb
#Establishing connection 
db = MySQLdb.connect("localhost","root","","arduino") 
#format ("LocalHost","arduino","Database-Password","Database-Name")

cursor = db.cursor() #Opening the cursor to Database

port = 'COM4'         #Declare the serial port
print "Connecting...", port            #This confirms the declaration
arduino = serial.Serial(port, 9600)  #Will read the serial data
print "arduino detected"               #Confirms the device
 
data = arduino.readline()  #Read data from the device

#Inserting the data into table
cursor.execute("INSERT INTO motionsensor (voltage) VALUES (%s)", [data]) 
#format ("INSERT INTO <table> (colomn) VALUES(type)",(initialized value)) 
#Here initialized value is data, which is used to read device.

db.commit()     #Commit to insert the data
	
cursor.close()  #Close the cursor
	 
