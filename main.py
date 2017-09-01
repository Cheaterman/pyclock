import os
import time
from random import randint

while 1 :
    h = int(input("heure : "))
    m = int(input("minute : "))
    s = int(input("seconde : "))
    while 1:
        heure = time.localtime()
        music = randint(0, 6)
        if (heure.tm_hour == h and heure.tm_min == m and heure.tm_sec == s):
            if (music == 0) :
                os.startfile("Enter_Sandman.flac")
            elif (music == 1) :
                os.startfile("A_demon_s_fate.flac")
            else :
                os.startfile("Blind.flac")
			# ...

            time.sleep(2)

            os.system("pause")
            os.system("taskkill /f /im foobar2000.exe")
            break
        else :
            time.sleep(1)
