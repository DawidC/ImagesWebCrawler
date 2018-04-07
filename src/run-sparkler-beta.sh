#!/usr/bin/env bash

if [ $# -ne 6 ]
then
    echo "Blad $#"
    exit 1
fi

    

while [ $# -gt 0 ]; do
    case "$1" in
	-su) shift; hostname="$1"; shift ;;
	-tn) shift; tn="$1"; shift ;;
	-i) shift; i="$1"; shift ;;
    esac
done

# Step 1. Run the script - it starts docker container and forwards ports to host
bash dockler.sh

#############################
container_id=`docker ps -q -l`
user="sparkler"

# Step 2. Inject seed urls
docker exec --user "$user" "$container_id" /data/sparkler/bin/sparkler.sh inject -id 1 -su "$hostname"
# Step 3. Start the crawl job
docker exec --user "$user" "$container_id" /data/sparkler/bin/sparkler.sh crawl -id 1 -tn "$tn" -i "$i"     # id=1, top 100 URLs, do -i=2 iterations
# Step 4. Export urls to .csv
curl -o results.csv 'http://localhost:8983/solr/crawldb/select?q=*:*&rows=20000&fl=url&wt=csv'


## prepare
#mkdir photos
