#!/usr/bin/python

import os
import git
import subprocess

filePath = os.path.dirname(os.path.realpath(__file__))
os.chdir(filePath) #Calling directory of script might be diff

#pass your repository for VCS
repo = git.Repo( filePath )
print repo.git.status()

# checkout and track your remote branch
print repo.git.checkout( )

#add all the changes back to branch

print repo.git.add( '-A' )

# commit
print repo.git.commit( m='my commit from python' )

# now we are one commit ahead
print repo.git.status()

print repo.git.push('master')

#print os.path.join




