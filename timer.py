import time
import os.path
import json

run = input("Start? Over or resume ? Press ctrl + c to cancel >> ")

# Only run if the user types in "start"
if run.lower() == "s" or run.lower() == 'start':
    timeit = {'mins' : 0,
            'hours' : 0,
            'seconds' : 0}
    
else :
    if os.path.exists('timeitfile.json'):
        with open('timeitfile.json') as timeitfile:
            timeit = json.load(timeitfile)

while True:
    # Sleep for a minute
    time.sleep(1)
    print("\x1b[2K\r {:02}:{:02}:{:02}".format(int(timeit['hours']), int(timeit['mins']), int(timeit['seconds'])), end='')
    timeit['seconds'] += 1
    if timeit['seconds'] % 5 == 0:
        with open('timeitfile.json', 'w+') as timeitfile:
            json.dump(timeit, timeitfile)

    # Increment the minute total
    if timeit['seconds'] % 60 == 0 :
        timeit['mins'] += 1
        timeit['seconds'] /= 60
    if timeit['mins'] % 60 == 0 and timeit['mins'] != 0:
        timeit['hours'] += 1
        timeit['mins'] /= 60