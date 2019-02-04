import time
import msgpack
import binascii
import json
import crcmod
import paho.mqtt.client as mqtt
import ssl



from threading import Thread

class MQTT_CLIENT(object):
    
   def __init__(self,ip,port,username,password,topic = None):
        self.ip = ip
        self.port = int(port)
        self.username = username
        self.password = password
        self.is_connected_flag = False
                

   def start(self):
         t = Thread(target=self.mqtt_control, args=())
         t.start()
         
   def mqtt_control(self):      
       client = mqtt.Client()
       self.client = client
       client.tls_set( cert_reqs=ssl.CERT_NONE )
       client.on_connect = self.on_connect
       client.on_message = self.on_message
       client.username_pw_set(self.username,self.password)
       print("$$$$$$$$$$$",self.username,self.password)
       print("$$$$$$$$$$$",self.ip,self.port)
       client.connect(self.ip,self.port, 60)
       client.loop_forever()
       
   def on_connect(self,client, userdata, flags, rc):
       print("Connected with result code "+str(rc)) 
       #client.subscribe("REMOTES/#", qos=0)
       client.subscribe("#")       
       self.is_connected_flag = True       

   # The callback for when a PUBLISH message is received from the server.
   def on_message(self, client, userdata, msg):
       #print("input raw ------------>",msg.topic,msg.payload)
       print("input decoded -------->",msg.topic, msgpack.unpackb(msg.payload))
       
   def publish(self,topic,payload):
      if self.is_connected_flag == True:
          self.client.publish(topic, payload, 0, False)

   def is_connected(self):
         return self.is_connected_flag