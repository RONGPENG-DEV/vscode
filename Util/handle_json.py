import sys
import os
base_path = os.getcwd()
sys.path.append(base_path)

import json
def read_json():
    with open(base_path+"/Config/user_data.json") as f:
        data =json.load(f)
    return data

def get_value(key):
    data = read_json()
    return data[key]


