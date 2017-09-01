# encoding: utf8

from __future__ import print_function
from threading import Thread
import datetime
import glob
import os
import platform
import random
import sys
import time

DATE_FORMAT = '%H:%M:%S'
MUSIC_FOLDER = 'music'
MUSIC_EXTENSION = 'flac'
MUSIC_PLAYER = '/usr/bin/mplayer'
ANY_KEY_COMMAND = (
    'pause'
    if platform.system() == 'Windows' else
    'read -n1'
)
KILL_PROGRAM_COMMAND = (
    'taskkill /f /im'
    if platform.system() == 'Windows' else
    'killall'
)

try:
    input = raw_input
except NameError:
    pass

should_tell_time = False
should_start_music = False


def tell_time():
    while True:
        if should_tell_time:
            print(
                '\rIl est actuellement: {}'.format(
                    datetime.datetime.now().strftime(DATE_FORMAT)
                ),
                end='',
            )
            sys.stdout.flush()
        time.sleep(1)

time_thread = Thread(target=tell_time)
time_thread.daemon = True
time_thread.start()


def start_music():
    while True:
        if should_start_music:
            filename = random.choice(music_files)
            print('Playing: {}'.format(filename))
            os.system('%s %s' % (MUSIC_PLAYER, filename))
            while should_start_music:
                time.sleep(.1)

music_thread = Thread(target=start_music)
music_thread.daemon = True
music_thread.start()


while True:
    target = None
    while not target:
        raw_data = input('Heure du réveil (HH:MM:SS) : ')
        try:
            target = datetime.time(
                *[int(item) for item in raw_data.split(':')]
            )
        except ValueError:
            pass
        except TypeError:
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
            should_start_music = True
            os.system(ANY_KEY_COMMAND)
            os.system(
                '%s %s' % (
                    KILL_PROGRAM_COMMAND,
                    os.path.split(MUSIC_PLAYER)[1],
                )
            )
            should_start_music = False
            break
        else:
            time.sleep(.5)

    should_tell_time = False
