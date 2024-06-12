import io
import os
import modules.constants as msgcon
from datetime import date, datetime
from modules.configuration import cfg
from modules.message import msg
from modules.writeDunders import writeDunders

__author__: str		= "Stephen D. Cooper <sdmagic@gmail.com>"
__copyright__: str	= "Copyright 2024 by Stephen D. Cooper. All rights reserved."
__status__: str		= "alpha"
__version__: str	= "0.0.1"
__date__: str		= "2024-05-07"	# YYYY-MM-DD

all = ("writeMain")

def writeMainHeader(outFile: io.TextIOWrapper) -> None:
	'''
	writeMainHeader() - Write the main header to the file.
	'''
	oLine = [f"'''\n",
			 f"The application's main entry point.\n",
			 f"'''\n\n",
			 f'import os\n']
	outFile.writelines(oLine)

	if cfg.trackRunTime:
		oLine = [f"import time\n"]
		outFile.writelines(oLine)

	oLine = [f"from {cfg.dirModules}.configuration import cfg\n\n"]
	outFile.writelines(oLine)

def writeMainEntry(outFile: io.TextIOWrapper) -> None:
	'''
	writeMainEntry() - Write the main() entry point to the file.
	'''

	oLine = [f"def main():\n"]
	outFile.writelines(oLine)

	print(f"cfg.trackRunTime = {cfg.trackRunTime}")
	if cfg.trackRunTime:
		oLine = [f"\tstart = time.time()\n"]
		outFile.writelines(oLine)

	oLine = [f"\tinitialzeConfiguration()\n"]
	outFile.writelines(oLine)

	if cfg.trackRunTime:
		oLine = ["\tprint(f'Program running time: {(time.time() - start): .2f} seconds')\n"]
		outFile.writelines(oLine)


	oLine = [f"\nif __name__ == '__main__':\n"
			 f"\tmain()\n"]
	outFile.writelines(oLine)

def writeMainInitialization(outFile: io.TextIOWrapper) -> None:

	oLine = [f"def initialzeConfiguration() -> None:\n",
			 f"\t'''\n",
			 f"\tInitialize the Configuration class.\n",

			 f"\tSpecifically, set the working and app directories and\n",
			 f"\tyaml file.\n",

			 f"\tThen, read the yaml file into the Configuration class.\n",
			 f"\t'''\n",
			 f"\tcfg.dirApp     = os.path.dirname(os.path.realpath(__file__)) # Set Application directory\n",
			 f"\tcfg.dirWorking = os.getcwd()	# Set working directory in Configuration\n",
			 f"\tcfg.yamlFile   = os.path.join(cfg.dirApp, f'{cfg.project}.yaml')\n\n",

			 f"\t# Paths are set -- Read the configuration file\n",
			 f"\t# This completes the initialization of the Configuration class\n",
			 f"\tcfg.readConfig()\n\n"]

	outFile.writelines(oLine)

def writeMain(mainFile: str) -> None:
	'''
	writeMain() writes the main.py file
	'''
	with open(mainFile, "w") as outFile:
		writeMainHeader(outFile)
		writeDunders(outFile)
		writeMainInitialization(outFile)
		writeMainEntry(outFile)


