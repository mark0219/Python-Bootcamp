# -*- coding: utf-8 -*-
"""
Created on Sat Jul 02 17:14:33 2016

@author: james.bradley
"""

file_path = 'C:\\Users\\jrbrad\\PythonBootCamp\\data\\'
f_in = open(file_path + 'hillaryclinton_sample_email_message_data.txt','r')

message_text = f_in.readlines()

for thisLine in message_text:
    print thisLine