# victron_mqtt_broker_calc
Script to calculate the Victron MQTT broker index used based on your VRM-portal-ID

A Victron installation will use a certain mqtt broker. (There are multiples for performance purposes)
You VRM Portal ID can be used to calculate the mqtt broker dns name.
This script will return the mqtt broker address for your installation.
Replace the VRM_portal_ID with your ID that you can find on your VRM online portal under settings/general.<br>
example of returned result: mqtt86.victronenergy.com
