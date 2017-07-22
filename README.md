# wifilogger
Collection of scripts to log wifi data into elasticsearch

Putting this together is pretty painful, this repo is really just a backup
for my various scripts.

The basic setup is you have a raspberry pi that runs kismet to log traffic.
We run kismet for 20 seconds at a time, have it log to disk, then restart.
This gives us a nice way to just look at all the previous files. We're not
worried about catching everything so losing time in startup and shutdown is
OK.

We then use tshark to parse the kismet pcap files and output something we
can hand to logstash. Filebeat is a great way to get data from the pi to
logstash. Logstash puts everything in elasticsearch, then we can create
dashboards and visualaizations.
