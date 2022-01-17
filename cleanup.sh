#!/bin/bash

# Remove swarm
sudo docker stack rm sprc3
sleep 20  # Make sure everything got removed by giving enough time

# Delete image
sudo docker image rm mqtt_adapter_image_sprc3
