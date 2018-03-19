#!/usr/bin/env bash

# Step 0. Get this script
wget https://raw.githubusercontent.com/USCDataScience/sparkler/master/bin/dockler.sh
# Step 1. Run the script - it starts docker container and forwards ports to host
bash dockler.sh
# Step 2. Inject seed urls
/data/sparkler/bin/sparkler.sh inject -id 1 -su 'http://www.bbc.com/news'
# Step 3. Start the crawl job
/data/sparkler/bin/sparkler.sh crawl -id 1 -tn 100 -i 2     # id=1, top 100 URLs, do -i=2 iterations

## prepare
#mkdir photos