#!/usr/bin/env python3
"""
Module Docstring
"""
import scanfile
import upload
from configparser import ConfigParser
import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
import time



__author__ = "Oliver"
__version__ = "0.0.1"
__license__ = "MIT"

def updateScanId(scanId):
    #Read config.ini file
    config_object = ConfigParser()
    config_object.read("config.ini")

    #Get the USERINFO section
    userinfo = config_object["USERINFO"]
    
    scanId = int(scanId)
    scanId = scanId + 1
    scanId = str(scanId)

    #Update the Scan Id
    userinfo["scanId"] = scanId

    #Write changes back to file
    with open('config.ini', 'w') as conf:
        config_object.write(conf)
        
def getFileName():
    #Read config.ini file
    config_object = ConfigParser()
    config_object.read("config.ini")
    
    #Get the user and hire
    userInfo = config_object["USERINFO"]
    userKey = userInfo["userkey"]
    hireId = userInfo["hireId"]
    scanId = userInfo["scanId"]
    
    #Get the device ID
    userinfo = config_object["DEVICE"]
    deviceId = userinfo["deviceId"]
    fileExtension = '.png'
    
    #Increment scan ID
    updateScanId(scanId)
    
    #Build the file name
    output = scanId + '-' + hireId + '-' + userKey + '-' + deviceId + fileExtension
    print ('Next file will be called ' + output)
    return (output)
    

def main():
    """ Main entry point of the app """
    print("hello world")
    
    
    print ('Waiting for button press')
    
    GPIO.setwarnings(False) # Ignore warning for now
    GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
    GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 10 to be an input pin and set initial value to be pulled low (off)
    
    while True: # Run forever
        if GPIO.input(10) == GPIO.HIGH:
            print("Button was pushed!")
            
            #avoid multi reading by sleeping
            time.sleep(1)
            
            #Get filename
            output = getFileName()
            
            #Scan the image in the scanner
            scanfile.main(output)
            upload.upload(output)
            
            
            print("Waiting for next button push...")

    
    


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()