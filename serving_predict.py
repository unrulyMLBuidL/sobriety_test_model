import json
import requests

host = 'http://localhost:{}/predict'

url = host


tester = {
"sex"   : "Male",
"age"   : 35,
"height" : 180,
"weight"  : 70,
"waistline" : 78.0,
"sight_left" : 1.0,
"sight_right" :1.0,
"hear_left"  : 1.0,
"hear_right" : 1.0,
"SBP"    : 108.0,
"DBP"      :            60.0,
"BLDS"      :           85.0,
"tot_chole"  :         159.0,
"HDL_chole"   :         67.0,
"LDL_chole"    :        78.0,
"triglyceride"  :       68.0,
"hemoglobin"     :      15.1,
"urine_protein"   :      1.0,
"serum_creatinine" :     0.9,
"SGOT_AST"          :   20.0,
"SGOT_ALT"           :  13.0,
"gamma_GTP"           : 13.0,
"SMK_stat_type_cd"     : 2.0
}

response = requests.post (url, json=tester).json()
sobriety_result = json.dumps(response, indent=4)

print(sobriety_result)