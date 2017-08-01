# -*- coding: utf-8 -*-
"""
Created on Thu Jul 07 09:27:40 2016

@author: james.bradley
"""

import os         # operating system package that helps us find files in a folder
import re         # import regular expressions package -- might be useful
import operator   # might be useful for sorting

# can use file_paths list to store file paths for folders you want to investigate
# I've started you off with one file path
file_paths = ['D:/TeachingMaterials/BusinessAnalytics/Programming/Python/PythonBootCamp/data/enron_mail_20150507/maildir/skilling-j/sent/']   
email_to = {}     # create empty dictionary for histogram data

for file_path in file_paths:
    for file_name in os.listdir(file_path):     # operating system command to return all the file names in a specified folder
        print (file_name)