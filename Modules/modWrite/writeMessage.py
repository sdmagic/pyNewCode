import io
import os
import modules.constants as msgcon
from datetime import date, datetime
from modules.configuration import cfg
from modules.writeDunders import writeDunders
from modules.message import msg

__author__: str		= "Stephen D. Cooper <sdmagic@gmail.com>"
__copyright__: str	= "Copyright 2024 by Stephen D. Cooper. All rights reserved."
__status__: str		= "alpha"
__version__: str	= "0.0.1"
__date__: str		= "2024-06-04"	# YYYY-MM-DD

all = ("writeMessage")

def writeMsgHeader(outFile: io.TextIOWrapper) -> None:
	'''
	writeMsgHeader() - Write the Message file header to the file.
	'''
	oLine = [f"'''\n",
			 f"The application's messaging & logging program file.\n",
			 f"'''\n\n",
			 f"import datetime\n",
			 f"import logging\n",
			 f"import os\n",
			 f"from modules.configuration import cfg\n",
			 f"from rich.pretty import pprint\n\n"]
	outFile.writelines(oLine)

def writeMessage(msgFile: str) -> None:
	'''
	writeMain() writes the main.py file

	Parameters:

	msgFile (str) - The name of the Python code file to write
	'''
	with open(msgFile, "w") as outFile:
		writeMsgHeader(outFile)
		# writeDunders(outFile)
		# writeConfigClass(outFile)
		# writeConfigTail(outFile)
