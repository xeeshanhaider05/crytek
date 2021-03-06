#!/usr/bin/env python

import os
import git
import subprocess
import gitconfig 
join = os.path.join

VCSPath =  gitconfig.git['host']

filePath = os.path.dirname(os.path.realpath(__file__))
os.chdir(filePath) #Calling directory of script might be diff

print filePath

#pass your repository for VCS
try:
   repo = git.Repo( filePath )
except git.exc.InvalidGitRepositoryError:
   repo = git.Repo.init( filePath )
   print "repository initiated"

print repo.git.status()

#clone the repo to given VCS path

try:
   print repo.git.checkout( )
except git.exc.GitCommandError:
   cloned_repo = repo.clone(VCSPath)
   print "cloned the remote repository "+VSCPath


# checkout and track your remote branch
#print repo.git.checkout( )

#add all the changes back to branch

#print repo.git.add( '-A' )

# commit
#print repo.git.commit( m='my commit from python' )

# now we are one commit ahead
#print repo.git.status()

#print repo.git.push('master')

#print os.path.join




