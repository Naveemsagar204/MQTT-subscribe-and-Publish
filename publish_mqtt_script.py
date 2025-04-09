import paho.mqtt.client as mqtt


def on_connect(user_name, client, rc):
    if rc == 0:
        print("broker is connected")
    else:
        print("broker is not connected")


def create_mqtt_connection(host: str, port: int):
    """
    This method will create the mqtt connection
    :param host: broker ip address ex: 192.168.1.101
    :param port: broker port ex: 1883
    :return:
    """
    mqtt_client = mqtt.Client(callback_api_version=mqtt.CallbackAPIVersion.VERSION2, client_id="your client id")
    mqtt_client.on_connect = on_connect
    mqtt_client.connect(host, port)
    return mqtt_client

def publish_process():
    """
    This method will call create mqtt function, if broker is connected then publish data to given topic
    :return: None
    """
    host = "192.168.1.101" # Your ip address
    port = 1883 # Your port
    topic = "mqtt/publish/hello"
    client = create_mqtt_connection(host, port)
    client.publish(topic, "Hello world")

if __name__ == "__main__":
    publish_process()

