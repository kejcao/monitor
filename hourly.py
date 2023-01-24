from data import khourly, mhourly, kstats, mstats
from datetime import datetime, timedelta

import matplotlib.pyplot as plt

ktimes = [
    datetime.fromisoformat(list(kstats)[0])+timedelta(hours=i)
    for i in range(len(khourly))
]

mtimes = [
    datetime.fromisoformat(list(mstats)[0])+timedelta(hours=i)
    for i in range(len(mhourly))
]

fig, axes = plt.subplots(3)

axes[0].set_ylabel('keys pressed')
axes[0].set_xlabel('date')
axes[0].plot(ktimes, [sum(h.values()) for h in khourly])

axes[1].set_ylabel('clicks')
axes[1].set_xlabel('date')
axes[1].plot(mtimes, [h['BTN_LEFT'] for h in mhourly], label='left click')
axes[1].plot(mtimes, [h['BTN_MIDDLE'] for h in mhourly], label='middle click')
axes[1].plot(mtimes, [h['BTN_RIGHT'] for h in mhourly], label='right click')
axes[1].legend()

axes[2].set_ylabel('scroll')
axes[2].set_xlabel('date')
axes[2].plot(mtimes, [h['REL_WHEEL'] for h in mhourly])

plt.show()
