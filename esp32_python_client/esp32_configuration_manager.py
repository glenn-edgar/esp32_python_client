
remote_configuration = {}

temp = {}
temp["mac"] = b'0\xae\xa4\x18\th'
temp_wifi = {}
temp_wifi[b"ssid"] = b"onyx_1_G"
temp_wifi[b"password"] = b"ready2go"
temp_wifi[b"hostname"] = b"esp32_switches"
temp[b"wifi"] = temp_wifi
temp_ibeacon = {}
temp_ibeacon[b"beacon_name"] = b"esp32_switches  "
temp[b"ibeacon"] = temp_ibeacon
temp_mqtt = {}
temp_mqtt[b"PORT"] = 8883
temp_mqtt[b"HOST"] = b"nano_data_center_demo.fios-router.home"
temp_mqtt[b"USER_NAME"] = b"pi"
temp_mqtt[b"PASSWORD"] = b"ready2go"
temp_mqtt[b"BASE_TOPIC"] = b"REMOTES/ESP32_SWITCHES/"
temp[b"mqtt"] = temp_mqtt
remote_configuration["esp32_switches"] = temp