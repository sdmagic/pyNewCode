import os
import modules as msgcon	# msgcon because we use msg for the class
from modules.configuration import cfg
from modules.message import msg

__author__: str		= "Stephen D. Cooper <sdmagic@gmail.com>"
__copyright__: str	= "Copyright 2024 by Stephen D. Cooper. All rights reserved."
__status__: str		= "alpha"
__version__: str	= "0.0.1"
__date__: str		= "2024-05-26"	# YYYY-MM-DD

all = ("writeInit")

def writeInit(initFile: str) -> None:
	'''
	writeInit() writes the modules\__init__.py file
	'''
	with open(initFile, "w") as outFile:
		pass
