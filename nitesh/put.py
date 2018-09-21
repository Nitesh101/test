#!/usr/bin/python

import os,time,mysql_py,sys
from ctypes import *
import time

localtime = time.asctime( time.localtime(time.time()) )
print "Script Start at :", localtime

os.chdir('/home/madisnit/Desktop/Executables_june_28_ble_server')
var=sys.argv
lis=var[1:]  # [init,1,dicover,1]
#Discover_List=[]
#Exception_list = [StopIteration, SystemExit, StandardError,ArithmeticError,OverflowError,FloatingPointError,ZeroDivisionError]
print "\n"
print "Going to Test ",lis

fun = CDLL("./testapp.so")

def call_init(index):
	loop = int(lis[index+1])
	#fun.mysql_Connect()
	for number in range(loop):
		if lis[index]=="init":
			print "\n..................initilizing .................\n"
			fun.VITA_DM_Init()
		else:
			print ".................wrong Entry  ................."
			sys.exit(0)

	
def call_discover(index):
	loop = int(lis[index+1])
#	print "length: ", loop
	for number in range(loop):
		if lis[index]=="discover":
			print "Delete All Tables before Discovering Devices ", number
			mysql_py.mysql_Truncate_Table("DM_Discover")
			mysql_py.mysql_Truncate_Table("DM_GET")
			mysql_py.mysql_Truncate_Table("DM_Observe")		
			time.sleep(3)

			fun.VITA_DM_Discover(fun.user_discover_callback);
			print "in sleep in python after discovery"
			for sec in range(5):
				time.sleep(1)
			Discover_List = mysql_py.mysql_Fetch_Discover()
	#		time.sleep(5)
			

			

		else:
			print "..................wrong discover called ................."
			sys.exit(0)

	if len(Discover_List) > 0:
		pass
	else:
							
        	raise Exception('Resources not found ' + str(lis))

def call_get(index):
	loop = int(lis[index+1])
	for number in range(loop):
		if lis[index]=="get":
			print "\n..................Going to GET Device Information..............."
			mysql_py.mysql_Truncate_Table("DM_GET")	
			#time.sleep(3)
			#print "Available Devices for GET"		
			Discover_List = mysql_py.mysql_Fetch_Discover()
			if len(Discover_List) > 0 :
			    for inputHandle in Discover_List:

			#	inputHandle = raw_input("input handle to get data : ")
			#	print "GET the device Information for Handle: ",inputHandle
			#	time.sleep(10)
				fun.VITA_DM_Get(inputHandle,fun.user_get_callback)	
				time.sleep(5)
		        	mysql_py.mysql_Fetch_Handle("DM_GET",inputHandle)
			#	time.sleep(5)
			else :
				
				raise Exception("Error:No resource found for getting device info")
		else:
			0
			print "..................wrong get  called ................."
			sys.exit(0)

def call_put(index):
	loop = int(lis[index+1])
	Put_fail = []
	for number in range(loop):
		if lis[index]=="put":
			print "*************************************"
			print "             PUT DATA                "
			print "*************************************"
			
			test = True
			Discover_List = mysql_py.mysql_Fetch_Discover()
			if len(Discover_List) > 0:
			   for inputHandle in Discover_List:
				print "DM_GET before PUT for Handle : ",inputHandle		
			     	mysql_py.mysql_Fetch_Handle("DM_GET",inputHandle)	
				print "........................................."
				print "Putting data for handle : ",inputHandle
				key = "power"
				valuetype = "i"
				value = mysql_py.mysql_fetech_value(inputHandle)
			mysql_py	
			print "change",key,"=",value,"to",key,"=",value + 50
				value = value + 50
				#print "type ", type(value)
				fun.put_data(inputHandle, key, valuetype, value, "NULL")
				time.sleep(3)
				mysql_py.mysql_Delete_Handle("DM_GET",inputHandle)
				time.sleep(2)
				fun.VITA_DM_Get(inputHandle,fun.user_get_callback)
				time.sleep(4)
				print "DM_GET after PUT for Handle :",inputHandle			
				key_val = mysql_py.mysql_Fetch_Handle("DM_GET",inputHandle)
				if(key_val == None):
					print 'val is none'
					key_val = '0'
				#print type(key_val),key_val, type(value), value 
				if(int(key_val) == value) :
					test = True
					pass
				else:
					Put_fail.append(inputHandle)
					test = False
				time.sleep(2)
			   if(test):
				  print "put sucess on all resources"
			   else:
				  
				  print "put failed on ", Put_fail
				  raise Exception("put failed on resources" + str(lis))	
				  	
			else:
				
				raise Exception("No Resource found to put" + str(lis))	
		else:
			print "..................wrong get  called ................."
			VITA_TL_Send(W_Put)
			sys.exit(0)
			#print "\nconnecting to mysql database\n"
#fun.mysql_Connect()
			
if((len(lis) % 2) == 0):
	for index in range(0,len(lis),2):	
		if(lis[index]=="init" or lis[index]=="w_init"):   	   # init	
			if index == 0:                      		   #connect to mysql database
			mysql_py	print "\nconnecting to mysql database\n"
				fun.mysql_Connect()
		
			call_init(index)
			elif(lis[index]=="discover" or lis[index]=="w_discover"):   # discover
			call_discover(index)
				
		elif(lis[index]=="get" or lis[index]=="w_get"):             # get
			call_get(index)
			
		elif lis[index]=="put" or lis[index]=="w_put":              # put
			call_put(index)
else :
        print "passed wrong command line arguments"
	raise Exception("Error: you have passed wrong command line arguments" + str(lis))
	raise Exception("Error: you have passed wrong command line arguments" + str(lis))

endtime = time.asctime( time.localtime(time.time()) )
print "Script End at :", endtime
	
