# encoding: utf8

from threading import Thread
import datetime
import glob
import os
import random
import time

DATE_FORMAT = '%H:%M:%S'
MUSIC_FOLDER = 'music'
MUSIC_EXTENSION = 'flac'
MUSIC_PLAYER = '/usr/bin/mplayer'

try:
    input = raw_input
except NameError:
    pass

should_tell_time = False

def tell_time():
    while True:
        if should_tell_time:
            print(
                'Il est actuellement: {}'.format(
                    datetime.datetime.now().strftime(DATE_FORMAT)
                )
            )
        time.sleep(1)

thread = Thread(target=tell_time)
thread.daemon = True
thread.start()


while True:
    target = None
    while not target:
        raw_data = input('Heure du réveil (HH:MM:SS) : ')
        try:
            target = datetime.time(*[int(item) for item in raw_data.split(':')])
        except ValueError:
            pass
    music_files = glob.glob(os.path.join(MUSIC_FOLDER, '*.' + MUSIC_EXTENSION))

    if not music_files:
        print(
            'Erreur: Aucun fichier présent dans le dossier {}.'.format(
                MUSIC_FOLDER
            )
        )
        continue

    should_tell_time = True

    while True:
        if(
            datetime.datetime.now()
            .strftime(DATE_FORMAT) == target.strftime(DATE_FORMAT)
        ):
            filename = random.choice(music_files)
            print('Playing: {}'.format(filename))
            os.system('%s %s' % (MUSIC_PLAYER, filename))
            break
        else:
            time.sleep(.5)

    should_tell_time = False
