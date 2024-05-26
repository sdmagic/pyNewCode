import io
import os
from datetime import date, datetime
from modules.configuration import cfg

__author__: str		= "Stephen D. Cooper <sdmagic@gmail.com>"
__copyright__: str	= "Copyright 2024 by Stephen D. Cooper. All rights reserved."
__status__: str		= "alpha"
__version__: str	= "0.0.1"
__date__: str		= "2024-05-07"	# YYYY-MM-DD

all = ("writeDunders")

def writeDunders(outFile: io.TextIOWrapper) -> None:
	'''
	Write a module's dunder variables to the file.
	'''

	copyright = f"Copyright {datetime.now().year} by {cfg.author}. All rights reserved."

	oLine = [f"__author__:    str = \"{cfg.author}\"\n",
			 f"__copyright__: str = \"{copyright}\"\n",
			 f"__version__:   str = \"{cfg.version}\"\n",
			 f"__date__:      str = \"{date.today()}\"	# YYYY-MM-DD\n\n"]
	outFile.writelines(oLine)
