import atexit
import json
from datetime import datetime, timedelta
from math import sqrt
from pathlib import Path

def save():
    with open('/home/kjc/mouse.stat', 'w') as fp:
        json.dump(stats, fp)
atexit.register(save)

stats = {}
if Path('/home/kjc/mouse.stat').exists():
    with open('/home/kjc/mouse.stat', 'r') as fp:
        stats = json.load(fp)

t = datetime.now()
while True:
    if datetime.now() > t:
        t = datetime.now() + timedelta(hours=1)
        stats[datetime.now().isoformat()] = {}
        save()

    event = input()
    if event == 'SYN_REPORT' or event.startswith('REL_WHEEL_HI_RES'):
        continue

    value = 1

    if event.startswith('REL_WHEEL'):
        event = 'REL_WHEEL'

    if event.startswith('REL_X') or event.startswith('REL_Y'):
        _, x = event.split()
        if (event := input()) != 'SYN_REPORT':
            _, y = event.split()
            value = sqrt(int(x)**2 + int(y)**2)
        else:
            value = abs(int(x))

        event = 'DIST'

    stat = list(stats.values())[-1]
    stat[event] = stat.get(event, 0) + value
