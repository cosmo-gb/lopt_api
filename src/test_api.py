#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 27 19:44:31 2023

@author: guillaume
"""


import requests
import json


def send_data(path_name_json, url):
    with open(path_name_json, 'r') as file:
        payload = json.load(file)
    url += '/productionplan'
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, json=payload, headers=headers)
    # check answer status
    if response.status_code == 200: # correct answer
        response_data = response.json()
        print(response_data)
        save_file = open("../responses/response_to_" + name + str(f) +".json", "w")  
        json.dump(response_data, save_file, indent = 2)  
        save_file.close() 
        return response_data
    else:
        # request failed
        print('request failed', response.status_code)
        return response.status_code

if __name__ == '__main__':
    path = '../example_payloads/'
    name = 'payload'
    f = 1 # payload number you want to post
    # request POST to the API
    # this url can be changed if it is also changed in the code api_post
    #url = 'http://192.168.79.240:8888'
    url = 'http://127.0.0.1:5000'
    #url = 'http://127.0.0.1:8888'  
    path_name_json = path + name + str(f) + '.json'
    send_data(path_name_json, url)
