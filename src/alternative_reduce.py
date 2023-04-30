#!/usr/bin/env python3

# command line args
import argparse
inspect = argparse.ArgumentParser()
inspect.add_argument('--hashtags', nargs='+', required=True)
arguments = inspect.parse_args()

# imports
import os
import json
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt 
from collections import defaultdict

info = {hashtag: defaultdict(int) for hashtag in arguments.hashtags}

for filename in os.listdir('outputs'):
    with open(os.path.join('outputs', filename)) as f:
        numbs = json.load(f)
        date = filename.split('.')[0]
        for hashtag in arguments.hashtags:
            if hashtag in numbs:
                total_count = sum(numbs[hashtag].values())
                info[hashtag][date] += total_count
            else:
                print(f"Hashtag {hashtag} not in data for {date}")

plt.figure()

for hashtag, numbs in info.items():
    if numbs:
        dates, values = zip(*sorted(numbs.items()))
        plt.plot(dates, values, label=hashtag)

plt.legend()
plt.xlabel('Date')
plt.ylabel('Number of tweets')
plt.title('Hashtag usage over time')

plt.savefig('alternative.png')
