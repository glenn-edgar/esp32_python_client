
pull_up = 0
pull_down = 1
pull_up_down = 2
pull_floating = 3


remote_configuration = {}

temp = {}
temp["mac"] = b'0\xae\xa4\x18\th'
temp_wifi = {}
temp_wifi[b"ssid"] = b"onyx_1_G"
temp_wifi[b"password"] = b"ready2go"
temp_wifi[b"hostname"] = b"op_override_panel"
temp[b"wifi"] = temp_wifi
temp_ibeacon = {}
temp_ibeacon[b"beacon_name"] = b"esp32_switches  "
temp[b"ibeacon"] = temp_ibeacon
temp_mqtt = {}
temp_mqtt[b"PORT"] = 8883
temp_mqtt[b"HOST"] = b"nano_data_center_demo.fios-router.home"
temp_mqtt[b"USER_NAME"] = b"pi"
temp_mqtt[b"PASSWORD"] = b"ready2go"
temp_mqtt[b"BASE_TOPIC"] = b"REMOTES/OP_OVERRIDE/"
temp[b"mqtt"] = temp_mqtt

temp_d_inputs = {}
temp_d_inputs[b"pins"] = [23,22,21,19,18,5,17,16]
temp_d_inputs[b"pullup"] = [ pull_up,pull_up,pull_up,pull_up, pull_up, pull_up,pull_up,pull_up ]
assert len(temp_d_inputs[b"pins"]) == len(temp_d_inputs[b"pullup"])
temp_d_inputs[b"debounce"] = 10

temp[b"d_inputs"] = temp_d_inputs

#temp["d_outputs"] = temp_d_outputs

#temp["d_pulse"] = temp_d_pulse

#temp["d_pwm"] = temp_d_pwm

#temp["d_analog] = temp_analog
remote_configuration["op_override_panel"] = temp