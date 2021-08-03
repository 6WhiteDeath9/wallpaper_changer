import os
import random
import ctypes
from time import sleep
SPI_SETDESKWALLPAPER = 20 

slike = os.listdir("C:\\Users\\Leonardo\\Desktop\\Sex\\wall\\")
print(slike)

while True: 
    slika = random.choice(slike)
    print(slika)

    put = "C:/Users/Leonardo/Desktop/Sex/wall/" + slika 
    ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, put, 0)
    print(put)
    sleep(24*60*60) 

