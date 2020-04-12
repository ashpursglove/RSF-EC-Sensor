import serial
import time



try:
    ser = serial.Serial('/dev/ttyUSB0',115200)
    read_serial=ser.readline()
    print('\n'*100)
    print('Sensors found on port 0 :-)')
    time.sleep(0.5)
    print('Have Fun!!!')
    time.sleep(1)
    


except Exception:
    ser = serial.Serial('/dev/ttyUSB1',115200)
    print('\n'*100)
    print('Sensors found on port 1 :-)')
    time.sleep(0.5)
    print('Have Fun!!!')
    time.sleep(1)
    
except :
    print('\n'*100)
    print('Sensors not found :-(')
    time.sleep(3)
    print('Have you tried turning it off and on again??')
    time.sleep(1000)


def return_data():
    read_serial=ser.readline()
    
    from_ard = str(read_serial)
    
    val = '0.00'
    val = from_ard

    
    if (len(val) == 0):
        return 'No Data'

        
    else:
        
        return val
    
return_data()

    
    

    
#     try:
#         print(from_ard)  
# 
#     except IndexError:
#         print('Getting Unstable')
#         print('Please Restart Me')

        
# return_data()