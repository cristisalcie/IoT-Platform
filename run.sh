#!/bin/bash

# Create image
sudo docker build . -t mqtt_adapter_image_sprc3

# Deploy swarm 
sudo docker stack deploy -c stack.yml sprc3
