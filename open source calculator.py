import os
import platform
import webbrowser

def open_calculator():
    system=platform.system()
    
    if system=="windows":
        os.system("start calc")
        
    elif system=="Darwin":
         os.system("open-a Calculator")
         
    elif system=="Linux":
         os.system("gnome-calculator")
         
    else:
         webbrowser.open("https://www.google.com/search?q=calculator")