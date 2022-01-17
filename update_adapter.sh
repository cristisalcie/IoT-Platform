#!/bin/bash

# Note: Because it is a swarm container name changes at runtime!

# Copy changes to docker container
docker cp src/mqtt_adapter.py sprc3_mqtt_adapter_sprc3.1.95nu0van2ts1tj3fc3lzz9jm9:/app/

# Restart container to apply changes only if dockerfile has command to run
# docker container restart sprc3_mqtt_adapter_sprc3.1.qku45ilx66w2busq86hqa9wj8
