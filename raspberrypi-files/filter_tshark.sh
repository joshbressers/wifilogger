#!/bin/sh

#filename=`basename $1`
filename=`date +%Y-%m-%d`

#tshark -Q -i wlan0 -T fields -e frame.time_epoch -e wlan_mgt.ssid -e radiotap.dbm_antsignal -e radiotap.datarate -e wlan.ra -e wlan.ta -e wlan.fc.type -e wlan.fc.type_subtype -E header=y -E separator=, > /home/pi/tshark-logs/output.log

tshark -Q -r $1 -T fields -e frame.time_epoch -e wlan_mgt.ssid -e ppi.80211-common.dbm.antsignal -e ppi.80211-common.dbm.antnoise -e ppi.80211-common.rate -e ppi.80211-common.chan.freq -e wlan_mgt.ds.current_channel -e wlan.ra -e wlan.ta -e wlan.fc.type -e wlan.fc.type_subtype -e wlan_mgt.rsn.pcs.type -e wlan_mgt.rsn.gcs.type -e wlan_mgt.rsn.akms.type -e wlan.sa_resolved -E header=y -E separator=, -E occurrence=f | sed -n '1!p' >> /home/pi/tshark-logs/$filename.log
