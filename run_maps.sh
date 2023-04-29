#!/bin/sh
    for file in '/data/Twitter dataset/'geoTwitter20*; do
        echo "Processing "$file""
        $(./src/map.py --input_path="$file") 
    done
