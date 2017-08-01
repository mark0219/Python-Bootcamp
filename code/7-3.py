# -*- coding: utf-8 -*-
"""
Created on Sat Jul 02 17:14:33 2016

@author: james.bradley
"""

f_in = open('D:\TeachingMaterials\BusinessAnalytics\Programming\Python\PythonBootCamp\data\hillaryclinton_sample_email_message_data.txt','r')

message_text = f_in.readlines()

for thisLine in message_text:
    print thisLine