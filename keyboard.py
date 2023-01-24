import atexit
import json
from datetime import datetime, timedelta
from pathlib import Path

def save():
    with open('/home/kjc/keys.stat', 'w') as fp:
        json.dump(stats, fp)
atexit.register(save)

stats = {}
if Path('/home/kjc/keys.stat').exists():
    with open('/home/kjc/keys.stat', 'r') as fp:
        stats = json.load(fp)

t = datetime.now()
while True:
    if datetime.now() > t:
        t = datetime.now() + timedelta(hours=1)
        stats[datetime.now().isoformat()] = {}
        save()

    key = input()
    stat = list(stats.values())[-1]
    stat[key] = stat.get(key, 0) + 1
