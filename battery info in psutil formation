import psutil
command=input("You :")
if "battery" in command:
    battery=psutil.sensors_battery()
    
    if battery:
        speak("battery imformation\n \n")
        print("battery percentage :",battery.percent,"%")
        
        if battery.power_plugged:
            print("status :Charging")
            
        else:
            print("status :Not charging")
             
    else:
         speak("battery information is not available")