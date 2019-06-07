import lidar
import time # Time module
#Serial port to which lidar connected, Get it from device manager windows
#In linux type in terminal -- ls /dev/tty* 
port = raw_input("Enter port name which lidar is connected:") #windows
#port = "/dev/ttyUSB0" #linux
Obj = lidar.YdLidarG4(port)
if(Obj.Connect()):
    print(Obj.GetDeviceInfo())
    '''print(Obj.GetCurrentFrequency())
    Obj.IncreaseCurrentFrequency(lidar.FrequencyStep.oneTenthHertz)
    print(Obj.GetCurrentFrequency())
    Obj.DecreaseCurrentFrequency(lidar.FrequencyStep.oneHertz)
    print(Obj.GetCurrentFrequency())
    print(Obj.GetCurrentRangingFrequency())
    Obj.SwitchRangingFrequency()
    print(Obj.GetCurrentRangingFrequency())
    Obj.DisableLowPowerMode()'''
    gen = Obj.StartScanning()
    t = time.time() # start time 
    while (time.time() - t) < 40: #scan for 30 seconds
        data=next(gen)
        print(data)
        time.sleep(0.5)
    
    '''print(Obj.GetCurrentFrequency())
    Obj.IncreaseCurrentFrequency(lidar.FrequencyStep.oneHertz)
    print(Obj.GetCurrentFrequency())
    print(Obj.GetDeviceInfo())
    gen = Obj.StartScanning()
    t = time.time() # start time
    while (time.time() - t) < 20: #scan for 30 seconds
        data=next(gen)
        print(data)
        time.sleep(0.5)'''
    Obj.Disconnect()
else:
    print("Error connecting to device")
