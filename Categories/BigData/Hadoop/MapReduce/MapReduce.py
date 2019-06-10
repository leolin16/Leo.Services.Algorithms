#%%
#map
import sys

for line in sys.stdin:
    line = line.strip()
    words = line.split()
    for word in words:
        print('%s\t%s') %(word, 1)

#%%

# reduce
from operator import itemgetter

current_word = None
current_count = 0
word = None

line = line.strip()
word, count = line.split('\t', 1)

try:
    count = int(count)
except ValueError:
    continue

# hadoop fs -ls /data/???
# hadoop fs -mkdir /data/hadoop/input/1
# hadoop fs -put *.txt /data/hadoop/input/1/
# hadoop fs -ls /data/hadoop/input/1/


