import os
from modules.configuration import cfg

__author__: str		= "Stephen D. Cooper <sdmagic@gmail.com>"
__copyright__: str	= "Copyright 2024 by Stephen D. Cooper. All rights reserved."
__status__: str		= "alpha"
__version__: str	= "0.0.1"
__date__: str		= "2024-05-20"	# YYYY-MM-DD

all = ("buildDir", "createDirs")

def buildDir(path: str) -> None:
	'''
	BuildDir creates a directory structure if it doesn't exist

	Parameters

		path (str): The path to the directory to be created
	'''

	if not os.path.exists(path):
		os.makedirs(path)

def createDirs() -> None:
	'''
	createDirs Creates the project's directories
	'''

	homeDir = os.getcwd()

	# buildDir(cfg.dirWorking)
	
	# os.chdir(cfg.dirWorking)

	# buildDir(cfg.dirConfig)
	# buildDir(cfg.dirLogs)
	# buildDir(cfg.dirModules)
	
	os.chdir(homeDir)
