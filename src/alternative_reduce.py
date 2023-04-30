#!/usr/bin/env python3

# command line args
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--hashtags', nargs='+', required=True)
args = parser.parse_args()

# imports
import os
import json
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from collections import defaultdict

data = {hashtag: defaultdict(int) for hashtag in args.hashtags}

for filename in os.listdir('outputs'):
    with open(os.path.join('outputs', filename)) as f:
        counts = json.load(f)
        date = filename.split('.')[0]
        for hashtag in args.hashtags:
            if hashtag in counts:
                total_count = sum(counts[hashtag].values())
                data[hashtag][date] += total_count
            else:
                print(f"Hashtag {hashtag} not in data for {date}")

plt.figure()

for hashtag, counts in data.items():
    if counts:
        dates, values = zip(*sorted(counts.items()))
        plt.plot(dates, values, label=hashtag)

plt.legend()
plt.xlabel('Date')
plt.ylabel('Number of tweets')
plt.title('Hashtag usage over time')

plt.savefig('alternative.png')
