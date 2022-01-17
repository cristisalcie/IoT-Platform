import paho.mqtt.client as mqtt
from influxdb import InfluxDBClient
import time
from datetime import datetime
import json


db_client = InfluxDBClient(host='influxdb_sprc3', port=8086)
db_client.create_database('sprc3')
db_client.switch_database('sprc3')


def on_connect(mqtt_client, userdata, flags, rc):
    if rc == 0:
        print("Connected OK!")
        mqtt_client.subscribe("#")
    else:
        print("Connection error! ", rc)

def on_disconnect(mqtt_client, userdata, flags, rc):
    print("Disconnected with status code = !", rc)

def on_message(mqtt_client, userdata, msg):
    location, station = msg.topic.split('/')

    decodedReceivedMessage = str(msg.payload.decode("utf-8"))
    decodedReceivedDict = json.loads(decodedReceivedMessage)
    print(f"received msg from broker: {decodedReceivedMessage}")
    
    json_payload = []

    if "timestamp" in decodedReceivedDict:
        timestamp = decodedReceivedDict["timestamp"]
    else:
        timestamp = datetime.now().strftime("%Y-%m-%dT%H:%M:%S%z")
    
    for key, value in decodedReceivedDict.items():
        # Only get numeric types
        if type(value) == int or type(value) == float:
            json_payload.append(
                {
                    "measurement" : f"{station}.{key}",
                    "tags": {
                        "location": location,
                        "station": station
                    },
                    "time": timestamp,
                    "fields": {
                        "value": float(value)
                    }
                }
            )
    ret = db_client.write_points(json_payload)
    print(f"Did it work to write to database? ..... {ret}")        
    # rs = db_client.query("SELECT * FROM sprc3")
    # print(rs.raw)

def example_1():
    time.sleep(1)
    data = {}
    data["BAT"] = 99
    data["HUMID"] = 40
    data["PRJ"] = "SPRC"
    data["TMP"] = 25.3
    data["status"] = "OK"
    data["timestamp"] = "2019-11-26T03:54:20+03:00"
    mqtt_client.publish("UPB/RPi_1", json.dumps(data))

def example_2():
    time.sleep(1)
    data = {}
    data["Alarm"] = 0
    data["AQI"] = 12
    data["RSSI"] = 1500
    mqtt_client.publish("Dorinel/Zeus", json.dumps(data))

mqtt_client = mqtt.Client("MqttDemoClient")
mqtt_client.on_connect = on_connect
mqtt_client.on_message = on_message
mqtt_client.on_disconnect = on_disconnect
mqtt_client.connect("mosquitto_sprc3")
mqtt_client.loop_start()

example_1()
example_2()
time.sleep(2)
