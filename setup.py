from __future__ import print_function
from distutils.core import setup, Extension
import sys,os,glob

#module name and a c++ files in current directory"
moduleOne = Extension('test', sources = glob.glob('*.cpp') ,
		      include_dirs=[''],
		      #language = "c++", 
	              extra_compile_args=["-fopenmp "], 
		      extra_link_args=["-fopenmp"] )

try:
    setup (name = 'test',
           version = '1.0',
           description = 'This is a test package',
           author='Zeeshan Haider',
           author_email='xeeshanhaider05@gmail.com',
           ext_modules = [moduleOne])
    print("BUILD SUCCESSFUL ", file=sys.stdout)
except:
    print("BUILD ERROR: Check source name, extension or build config, further Info: ", sys.exc_info()[0], file=sys.stderr)
    


   
