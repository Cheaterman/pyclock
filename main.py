# encoding: utf8

import datetime
import glob
import os
import random
import time

DATE_FORMAT = '%H:%M:%S'
MUSIC_FOLDER = 'music'
MUSIC_EXTENSION = 'flac'

try:
    input = raw_input
except NameError:
    pass


while True:
    raw_data = input(u'Heure du réveil (HH:MM:SS) : '.encode('utf8'))
    target = datetime.time(*[int(item) for item in raw_data.split(':')])
    music_files = glob.glob(os.path.join(MUSIC_FOLDER, '*.' + MUSIC_EXTENSION))

    if not music_files:
        print(
            u'Erreur: Aucun fichier présent dans le dossier {}.'.format(
                MUSIC_FOLDER
            )
        )
        continue

    while True:
        if(
            datetime.datetime.now()
            .strftime(DATE_FORMAT) == target.strftime(DATE_FORMAT)
        ):
            filename = random.choice(music_files)
            print('Playing: {}'.format(filename))
            os.startfile(filename)

            time.sleep(2)

            os.system("pause")
            os.system("taskkill /f /im foobar2000.exe")
            break
        else:
            time.sleep(1)
