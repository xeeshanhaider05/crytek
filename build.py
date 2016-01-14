#!/usr/bin/python

import os
import subprocess, glob, sys

#Getting all sourc files from src directory: same where script lies
filePath = os.path.dirname(os.path.realpath(__file__))
os.chdir(filePath) #Calling directory of script might be diff
sources =  (glob.glob('*.cpp'))

#bin folder holds the executable of project
newpath = filePath+'/bin' 
if not os.path.exists(newpath):
    os.makedirs(newpath)

#open the process and generate the executable named "application"
p = subprocess.Popen([r"g++", "-Wall","-O2", "-o", newpath+"/application"]+sources, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
errorString = p.stderr.read() #collect all compiler outs as well
succString = p.stdout.read()
p.communicate()

#Print some output depending on the process
if errorString != "":
   sys.stderr.write(errorString+ "### BUILD FAILED ###\n" )
else:
   sys.stdout.write(succString+"### BUILD SUCCESSFUL ###\n")








