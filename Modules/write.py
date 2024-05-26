import io
import os
from datetime import date, datetime
from modules.configuration import cfg
from modules.writeConfig import writeConfig
from modules.writeInit import writeInit
from modules.writeMain import writeMain

__author__: str		= "Stephen D. Cooper <sdmagic@gmail.com>"
__copyright__: str	= "Copyright 2024 by Stephen D. Cooper. All rights reserved."
__status__: str		= "alpha"
__version__: str	= "0.0.1"
__date__: str		= "2024-05-07"	# YYYY-MM-DD

all = ("writeFiles")

def writeFiles() -> None:
	'''
	writeFiles() - Write the files for the project.
	'''
	homeDir = os.getcwd()
	
	if cfg.buildMain:
		writeMain()

	if cfg.buildConfig:
		writeConfig()

	if cfg.buildInit:
		writeInit()

	os.chdir(homeDir)