
pull_up = 0
pull_down = 1
pull_up_down = 2
pull_floating = 3

#temp_d_inputs = {}
#temp_d_inputs[b"pins"] = [23,22,21,19,18,5,17,16]
#temp_d_inputs[b"pullup"] = [ pull_up,pull_up,pull_up,pull_up, pull_up, pull_up,pull_up,pull_up ]
#assert len(temp_d_inputs[b"pins"]) == len(temp_d_inputs[b"pullup"])
#temp_d_inputs[b"debounce"] = 10

#temp[b"d_inputs"] = temp_d_inputs

remote_configuration = {}





temp = {}
temp["mac"] = b'0\xae\xa4\x90\xc0\xc4'
temp_wifi = {}
temp_wifi[b"ssid"] = b"onyx_4_G"
temp_wifi[b"password"] = b"ready2go"
temp_wifi[b"hostname"] = b"CURRENT_MONITOR_1"
temp[b"wifi"] = temp_wifi
temp_ibeacon = {}
temp_ibeacon[b"beacon_name"] = b"esp32_current_1 "

temp[b"ibeacon"] = temp_ibeacon
temp_mqtt = {}
temp_mqtt[b"PORT"] = 8883
temp_mqtt[b"HOST"] = b"farm_control.fios-router.home"
temp_mqtt[b"USER_NAME"] = b"pi"
temp_mqtt[b"PASSWORD"] = b"ready2go"
temp_mqtt[b"BASE_TOPIC"] = b"/REMOTES/CURRENT_MONITOR_1/"
temp[b"mqtt"] = temp_mqtt


temp[b"d_current_monitor"] = {}
temp[b"d_current_monitor"][b"max_current_equipment"] = 4.0
temp[b"d_current_monitor"][b"max_current_irrigation"] =4.0
temp[b"a_ad_inputs"] = {}
ad_conf_0 = { "attenuation":3, "channel":0 }  
ad_conf_1 = { "attenuation":3, "channel":3 }  
temp[b"a_ad_inputs"]["ANALOG_CHANNELS"] = [ad_conf_0 ,ad_conf_1 ]
temp["com"] = "COM4"
#
remote_configuration["CURRENT_MONITOR_1"] = temp






temp = {}
temp["mac"] =b'0\xae\xa4\xf8\x0bl'

temp_modbus = {}
temp_modbus[b"RTU_FLAG"] = True
temp_modbus[b"ADDRESS"] = 121
temp_modbus[b"BAUD_RATE"] = 38400
temp_modbus[b"PARITY"] = 0
temp[b"MODBUS_RELAY"] = temp_modbus
temp["com"] = "COM4"
remote_configuration["MODBUS_RELAY"] = temp


'''

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

temp[b"a_dac_outputs"] = {}
pwm_conf_1 = { "value":0x10 , "channel":1 }  
pwm_conf_2 = { "value":0xff , "channel":2 } 
temp[b"a_dac_outputs"]["DAC_OUTPUTS"] = [pwm_conf_1,pwm_conf_2]

temp[b"a_ad_inputs"] = {}
ad_conf_0 = { "attenuation":3, "channel":0 }  
ad_conf_1 = { "attenuation":3, "channel":3 }  
ad_conf_2 = { "attenuation":3, "channel":6 }  
ad_conf_3 = { "attenuation":3, "channel":7 }  
ad_conf_4 = { "attenuation":3, "channel":4 }  
ad_conf_5 = { "attenuation":3, "channel":5 }  
temp[b"a_ad_inputs"]["ANALOG_CHANNELS"] = [ad_conf_0 ,ad_conf_1 ,ad_conf_2 ,ad_conf_3,ad_conf_4,ad_conf_5  ]


#
temp["com"] = "COM4"
remote_configuration["PUMP_MONITOR_1"] = temp


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
temp["mac"] = b'\x80}:\xcf\x0b\xe8'

temp_wifi = {}
temp_wifi[b"ssid"] = b"onyx_1_G"
temp_wifi[b"password"] = b"ready2go"
temp_wifi[b"hostname"] = b"LUA_DEMO"
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


temp_task_1 = {b"LUA_TASK_NAME": b"LUA_TASK_1", b"LUA_TASK_FILE": b"/spiffs/TASK_1.LUA" }
temp[b"LUA_TASKS"] ={} 
temp[b"LUA_TASKS"][b"LUA_TASKS"] = [ temp_task_1 ]

temp[b"LUA_FILES"] = [ "TASK_1.LUA", "common.lua"]

temp["com"] = "COM3"
remote_configuration["LUA_DEMO"] = temp
'''