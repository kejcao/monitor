from data import kstats, kall, mstats, mall
from collections import Counter

print(kall)
print(f'from {list(kstats)[0]} to {list(kstats)[-1]}')
for key, freq in Counter(kall).most_common():
    print(f' {key: <16} {freq}')
print(' '*18 + f'{sum(kall.values())}')

print()

print(f'from {list(mstats)[0]} to {list(mstats)[-1]}')
print(f' moved {mall["DIST"]}px ({mall["DIST"]/(2560/20.748)/39370.1}km)')
print(f' scrolled {mall["REL_WHEEL"]} times')
print(f' L {mall["BTN_LEFT"]} | M {mall["BTN_MIDDLE"]} | R {mall["BTN_RIGHT"]}')
