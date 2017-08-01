# -*- coding: utf-8 -*-
"""
Created on Thu Jul 07 09:27:40 2016

@author: james.bradley
"""

import os     # operating system package that helps us find files in a folder
import re     # import regular expressions package
import operator

file_paths = ['D:/TeachingMaterials/BusinessAnalytics/Programming/Python/PythonBootCamp/data/enron_mail_20150507/maildir/skilling-j/sent/',
              'D:/TeachingMaterials/BusinessAnalytics/Programming/Python/PythonBootCamp/data/enron_mail_20150507/maildir/skilling-j/sent_items/',
              'D:/TeachingMaterials/BusinessAnalytics/Programming/Python/PythonBootCamp/data/enron_mail_20150507/maildir/skilling-j/_sent_mail/']
email_to = {}      # create dictionary for histogram
for file_path in file_paths:
    for file_name in os.listdir(file_path):
        print (file_name)
        # put your code here to mine each email file
        thisFile = open(file_path+file_name,'r')
        for thisLine in thisFile:
            findSomething = []
            email_add = []
            findSomething = re.findall('To:',thisLine)
            if len(findSomething) > 0:
                email_add = re.findall('[a-zA-Z0-9]\S*@\S*[a-zA-Z]',thisLine)
                if len(email_add) > 0:
                    for this_address in email_add:
                        email_to[this_address] = email_to.get(this_address.rstrip('\n'),0) + 1
                        #email_to.append(this_address)
                    
email_to_sorted = sorted(email_to.items(),key=operator.itemgetter(1),reverse=True)
print email_to_sorted