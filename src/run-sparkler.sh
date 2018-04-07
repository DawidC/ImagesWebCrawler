#!/usr/bin/env bash


# Step 1. Run the script - it starts docker container and forwards ports to host
bash dockler.sh

#############################
container_id=`docker ps -q -l`
user="sparkler"

# Step 2. Inject seed urls
docker exec --user "$user" "$container_id" /data/sparkler/bin/sparkler.sh inject -id 1 -su 'http://www.bbc.com/news'
# Step 3. Start the crawl job
docker exec --user "$user" "$container_id" /data/sparkler/bin/sparkler.sh crawl -id 1 -tn 10 -i 1     # id=1, top 100 URLs, do -i=2 iterations
# Step 4. Export urls to .csv
curl -o results.csv 'http://localhost:8983/solr/crawldb/select?q=*:*&rows=20000&fl=url&wt=csv'


## prepare
#mkdir photos
