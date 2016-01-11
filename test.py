#!/usr/bin/python
import calendar
import os
from git import Repo


print ("Hello World")
inp = raw_input("Press enter to exit")
var = 100

if(var == 100):
   print "Cool", inp

calen = calendar.month(2015,12)
print "The month"
print calen

Money = 2000
def AddMoney():
   # Uncomment the following line to fix the code:
   global Money
   Money = Money + 1

print Money
AddMoney()
print Money

print os.getcwd()

Repo.clone_from(https://github.com/xeeshanhaider05/crytek.git, /home/home/Work)
