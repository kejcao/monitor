import json
from collections import defaultdict
from datetime import datetime, timedelta

with open('/home/kjc/keys.stat', 'r') as fp:
    kstats = json.load(fp)

khourly = [{}]
t = datetime.fromisoformat(list(kstats)[0])
for date, stat in kstats.items():
    if stat:
        while not (t <= datetime.fromisoformat(date) <= t+timedelta(hours=1)):
            khourly.append({})
            t+=timedelta(hours=1)
        khourly[-1].update(stat)

kall = {}
for h in khourly:
    for k, v in h.items():
        kall[k] = kall.get(k, 0) + v

with open('/home/kjc/mouse.stat', 'r') as fp:
    mstats = json.load(fp)

mhourly = [defaultdict(int)]
t = datetime.fromisoformat(list(mstats)[0])
for date, stat in mstats.items():
    if stat:
        while not (t <= datetime.fromisoformat(date) <= t+timedelta(hours=1)):
            mhourly.append(defaultdict(int))
            t+=timedelta(hours=1)
        mhourly[-1].update(stat)

mall = {}
for h in mhourly:
    for k, v in h.items():
        mall[k] = mall.get(k, 0) + v
