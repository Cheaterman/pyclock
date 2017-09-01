# encoding: utf8

import datetime
import os
import random
import time

DATE_FORMAT = '%H:%M:%S'

try:
    input = raw_input
except NameError:
    pass


while True:
    raw_data = input(u'Heure du réveil (HH:MM:SS) : '.encode('utf8'))
    target = datetime.time(*[int(item) for item in raw_data.split(':')])

    while True:
        music = random.randint(0, 6)
        if(
            datetime.datetime.now()
            .strftime(DATE_FORMAT) == target.strftime(DATE_FORMAT)
        ):
            if music == 0:
                os.startfile("Enter_Sandman.flac")
            elif music == 1:
                os.startfile("A_demon_s_fate.flac")
            else:
                os.startfile("Blind.flac")
            # ...

            time.sleep(2)

            os.system("pause")
            os.system("taskkill /f /im foobar2000.exe")
            break
        else:
            time.sleep(1)
