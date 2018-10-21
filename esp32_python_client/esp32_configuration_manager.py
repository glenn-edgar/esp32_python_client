
pull_up = 0
pull_down = 1
pull_up_down = 2
pull_floating = 3

b'0\xae\xa4\x15\x16l'

remote_configuration = {}

temp = {}
temp["mac"] = b'0\xae\xa4\x18\th'
temp_wifi = {}
temp_wifi[b"ssid"] = b"onyx_1_G"
temp_wifi[b"password"] = b"ready2go"
temp_wifi[b"hostname"] = b"OP_OVERRIDE_1"
temp[b"wifi"] = temp_wifi
temp_ibeacon = {}
temp_ibeacon[b"beacon_name"] = b"esp32_switches  "

temp[b"ibeacon"] = temp_ibeacon
temp_mqtt = {}
temp_mqtt[b"PORT"] = 8883
temp_mqtt[b"HOST"] = b"nano_data_center_demo.fios-router.home"
temp_mqtt[b"USER_NAME"] = b"pi"
temp_mqtt[b"PASSWORD"] = b"ready2go"
temp_mqtt[b"BASE_TOPIC"] = b"REMOTES/OP_OVERRIDE_1/"
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
remote_configuration["OP_OVERRIDE_1"] = temp

temp = {}
temp["mac"] = b'0\xae\xa4\x15\x16l'

temp_wifi = {}
temp_wifi[b"ssid"] = b"onyx_1_G"
temp_wifi[b"password"] = b"ready2go"
temp_wifi[b"hostname"] = b"PI_RESET_1"
temp[b"wifi"] = temp_wifi
temp_ibeacon = {}
temp_ibeacon[b"beacon_name"] = b"esp32_switches  "

temp[b"ibeacon"] = temp_ibeacon
temp_mqtt = {}
temp_mqtt[b"PORT"] = 8883
temp_mqtt[b"HOST"] = b"nano_data_center_demo.fios-router.home"
temp_mqtt[b"USER_NAME"] = b"pi"
temp_mqtt[b"PASSWORD"] = b"ready2go"
temp_mqtt[b"BASE_TOPIC"] = b"REMOTES/PI_RESET_1/"
temp[b"mqtt"] = temp_mqtt

temp_d_outputs = {}
temp_d_outputs[b"pins"] = [23,22,21,19,18,5,17,16]
temp_d_outputs[b"init_values"] = [ 1,1,1,1, 1,1,1,1  ]
assert len(temp_d_outputs[b"pins"]) == len(temp_d_outputs[b"init_values"])


temp[b"d_outputs"] = temp_d_outputs

#
remote_configuration["PI_RESET_1"] = temp

temp = {}
temp["mac"] = b'0\xae\xa4\x90\xc0\xc4'

temp_wifi = {}
temp_wifi[b"ssid"] = b"onyx_1_G"
temp_wifi[b"password"] = b"ready2go"
temp_wifi[b"hostname"] = b"PUMP_MONITOR_1"
temp[b"wifi"] = temp_wifi
temp_ibeacon = {}
temp_ibeacon[b"beacon_name"] = b"esp32_switches  "

temp[b"ibeacon"] = temp_ibeacon
temp_mqtt = {}
temp_mqtt[b"PORT"] = 8883
temp_mqtt[b"HOST"] = b"nano_data_center_demo.fios-router.home"
temp_mqtt[b"USER_NAME"] = b"pi"
temp_mqtt[b"PASSWORD"] = b"ready2go"
temp_mqtt[b"BASE_TOPIC"] = b"REMOTES/PUMP_MONITOR_1/"
temp[b"mqtt"] = temp_mqtt

temp[b"d_pwm_outputs"] = {}
pwm_conf_1 = { "duty_a": 75. , "duty_b": 25., "frequency": 4000, "pin_a": 4, "pin_b":0 }  
pwm_conf_2 = { "duty_a": 25. , "duty_b": 75., "frequency": 4000, "pin_a": 2, "pin_b":15}  
temp[b"d_pwm_outputs"]["PWM_OUTPUTS"] = [pwm_conf_1,pwm_conf_2]

temp[b"d_counter_inputs"] = {}

temp[b"d_counter_inputs"][b"COUNTER_UPDATE_RATE"] = 15
temp[b"d_counter_inputs"][b"COUNTER_FILTER_COUNT"] = 10
temp[b"d_counter_inputs"][b"GPIO_PINS"] = [23,22,21,19]

#
temp["com"] = "COM4"
remote_configuration["PUMP_MONITOR_1"] = temp