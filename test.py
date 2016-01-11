#!/usr/bin/python

import os
import git

#pass your repository for VCS
repo = git.Repo( '/home/home/Work' )
print repo.git.status()

# checkout and track your remote branch
print repo.git.checkout( )

#add all the changes back to branch

print repo.git.add( '-A' )

# commit
print repo.git.commit( m='my commit from python' )

# now we are one commit ahead
print repo.git.status()








