#!/usr/bin/env python3

# command line args
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--input_path',required=True)
parser.add_argument('--key',required=True)
parser.add_argument('--percent',action='store_true')
args = parser.parse_args()

#imports
import os
import json
from collections import Counter,defaultdict
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# open the input path
with open(args.input_path) as f:
    counts = json.load(f)

# normalize the counts by the total values
if args.percent:
    for k in counts[args.key]:
        counts[args.key][k] /= counts['_all'][k]

# print the count values
items = sorted(counts[args.key].items(), key=lambda item: (item[1],item[0]), reverse=True)
for k,v in items:
    print(k,':',v)

top_data = sorted(counts[args.key].items(), key=lambda x: x[1], reverse=True)[:10]

keys, values = zip(*top_data)

plt.bar(keys, values, color='springgreen')

label_x = 'Language' if args.input_path.endswith('g') else 'Country'
label_y = 'Percent of Total' if args.percent else 'Tweet Volume'
plt.xlabel(label_x)
plt.ylabel(label_y)

filename = f"{args.key[1:]}_{label_x.lower()}.png"

plt.savefig(filename)
