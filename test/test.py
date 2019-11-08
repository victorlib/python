import json
import os

pwd = os.getcwd()
file_name = 'Control_Access.txt'
with open(file_name) as f:
    dict = json.load(f)
    for key in dict:
        print('map_arr[2][_T("'+key+'")]')
