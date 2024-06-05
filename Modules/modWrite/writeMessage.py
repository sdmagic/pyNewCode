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

def writeMsgClassHead(outFile: io.TextIOWrapper) -> None:
	oLine = [f"\t'''\n",
			 f"\tMessenger is a singleton class -- Only one per application\n\n",
			 f"\tTests whether to print to the screen using pprint() or print()\n",
			 f"\tAfter instantiation, the class will set the _printIt variable to either\n",
			 f"\tor None, depending on the user's configuration settings.\n\n",
			 f"\tUse Messenger.output() to print to the screen.\n\n",
			 f"\tNOTES:\n\n",
			 f"\t\tDO NOT USE __printIt directly. Use Messenger.output()\n\n",
			 f"\t\tmessage.py REQUIRES a cfg object that has these properties:\n\n",
			 f"\t\t\tcfg.dirApp       (str)  - Application directory\n",
			 f"\t\t\tcfg.dirLogs      (str)  - Log file directory\n",
			 f"\t\t\tcfg.logging      (bool) - Log messages?\n",
			 f"\t\t\tcfg.screenPretty (bool) - Use pprint()?\n",
			 f"\t\t\tcfg.screenPrint  (bool) - Prin to screen?\n\n",
			 f"\tPrivate Attributes:\n\n",
			 f"\t\t__instance (class)	 - Singleton instance\n",
			 f"\t\t__printIt (function) - The function to use to print to the screen.\n\n",
			 f"\tMethods:\n\n",
			 f"\t\toutput(msg) - Prints the message to the screen and log file.\n",
			 f"\t'''\n\n"]
	outFile.writelines(oLine)

def writeMsgClassMain(outFile: io.TextIOWrapper) -> None:
	oLine = [f"\t__instance = None	# Singleton instance\n",
			 f"\t__printIt  = None	# Function that prints to the screen\n\n",
			 f"\tdef __new__(cls):\n",
			 f"\t\tif Messenger.__instance is None:\n",
			 f"\t\t\tMessenger.__instance = super(Messenger, cls).__new__(cls)\n\n",
			 f"\t\treturn Messenger.__instance\n\n"]
	outFile.writelines(oLine)

def writeMsgConfigConfig(outFile: io.TextIOWrapper) -> None:
	oLine = [f"\t@classmethod\n",
			 f"\tdef config(cls) -> None:\n",
			 f"\t\tMessenger.configPrintFunction()\n",
			 f"\t\tMessenger.configLogs()\n\n"]
	outFile.writelines(oLine)

def writeMsgConfigLogs(outFile: io.TextIOWrapper) -> None:
	oLine = [f"\t@classmethod\n",
			 f"\tdef configLogs(cls) -> None:\n",
			 f"\t\t'''\n",
			 f"\t\tconfigLogs() configures the logging system.\n",
			 f"\t\t'''\n",
			 f"\t\t# ** Stupid Programmer Tricks to make the editor easier to use\n",
			 f"\t\t#\t\t\t** These are long lines, so we use variables\n",
			 f"\t\t#\t\t\t** to shorten the call to logging.basicConfig()\n",
			 f"\t\tlogFname: str = os.path.join(cfg.dirApp, cfg.dirLogs, \n",
			 "\t\t\t\t\tf'log{datetime.datetime.now().strftime(\"%Y%m%d\")}.log')\n",
			 f"\t\tlogFormat: str = '%(asctime)s (%(levelname)s) %(message)s'\n\n",
			 f"\t\tif cfg.logging:\n",
			 f"\t\t	logging.basicConfig(level=logging.DEBUG,\n",
			 f"\t\t\t\t\t\t\t\tfilename=logFname,\n",
			 f"\t\t\t\t\t\t\t\tencoding='utf-8',\n",
			 f"\t\t\t\t\t\t\t\tfilemode='a',\n",
			 f"\t\t\t\t\t\t\t\tformat=logFormat,\n",
			 f"\t\t\t\t\t\t\t\tdatefmt='%Y-%m-%d %H:%M:%S')\n\n"]
	outFile.writelines(oLine)

def writeMsgConfigPrint(outFile: io.TextIOWrapper) -> None:
	oLine = [f"\t@classmethod\n",
			 f"\tdef configPrintFunction(cls) -> None:\n",
			 f"\t\t'''\n",
			 f"\t\tconfigPrintFunction() configures the print function.\n",
			 f"\t\t'''\n",
			 f"\t\tif cfg.screenPretty:\n",
			 f"\t\t\tMessenger.__printIt: function = pprint\n",
			 f"\t\telif cfg.screenPrint:\n",
			 f"\t\t\tMessenger.__printIt: function = print\n",
			 f"\t\telse:\n",
			 f"\t\t\tMessenger.__printIt: NoneType = None\n\n"]
	outFile.writelines(oLine)

def writeMsgConfig(outFile: io.TextIOWrapper) -> None:
	writeMsgConfigConfig(outFile)
	writeMsgConfigLogs(outFile)
	writeMsgConfigPrint(outFile)

def writeMsgOutLog(outFile: io.TextIOWrapper) -> None:
	oLine = [f"\tdef outLog(self, msgType: str = msgcon.LOGINFO, message: str | dict = \"\") -> None:\n",
			 f"\t\t'''\n",
			 f"\t\tThis is the ONLY safe way to\n",
			 f"\t\tprint to the Log file.\n\n",
			 f"\t\tArgs:\n",
			 f"\t\t\tmsgType (str) - The type of log message\n",
			 f"\t\t\tmessage (str) - The message to print.\n\n",
			 f"\t\tExamples:\n",
			 f"\t\t\t>>> msg.outLog(msgType = 'info', 'Hello world!')\n",
			 f"\t\t\t'Hello world!'\n\n",
			 f"\t\t\t>>> msg.outLog(message = 'Mongo only pawn... in game of life.')\n",
			 f"\t\t\t'Mongo only pawn... in game of life.'\n\n",
			 f"\t\t\t>>> msg.outLog(msgType = 'warning', message = 'Without followers, evil cannot spread.')\n",
			 f"\t\t\t'Without followers, evil cannot spread.'\n",
			 f"\t\t'''\n\n",
			 f"\t\tif cfg.logging:\n",
			 f"\t\t\tif type(message) == str:\n",
			 f"\t\t\t\tmsgType = msgType.lower()\n",
			 f"\t\t\t\tif msgType == msgcon.LOGCRITICAL:\n",
			 f"\t\t\t\t\tlogging.critical(message)\n",
			 f"\t\t\t\telif msgType == msgcon.LOGDEBUG:\n",
			 f"\t\t\t\t\tlogging.debug(message)\n",
			 f"\t\t\t\telif msgType == msgcon.LOGERROR:\n",
			 f"\t\t\t\t\tlogging.error(message)\n",
			 f"\t\t\t\telif msgType == msgcon.LOGINFO:\n",
			 f"\t\t\t\t\tlogging.info(message)\n",
			 f"\t\t\t\telif msgType == msgcon.LOGNOLOG:	# Our own log type -- Don't log\n",
			 f"\t\t\t\t\tpass\n",
			 f"\t\t\t\telif msgType == msgcon.LOGWARNING:\n",
			 f"\t\t\t\t	\togging.warning(message)\n",
			 f"\t\t\t\telse:\n",
			 f"\t\t\t\t\tlogging.error('Unknown message')\n\n"]
	outFile.writelines(oLine)

def writeMsgOutPrint(outFile: io.TextIOWrapper) -> None:
	oLine = [f"\tdef outPrint(self, message: str | dict = \"\") -> None:\n",
			 f"\t\t'''\n",
			 f"\t\tThis is the ONLY safe way to print to the screen.\n\n",
			 f"\t\tArgs:\n",
			 f"\t\t\tmessage (str) - The message to print.\n\n",
			 f"\t\tExamples:\n",
			 f"\t\t\t>>> msg.output('Hello world!')\n",
			 f"\t\t\t'Hello world!'\n\n",
			 f"\t\t\t>>> msg.output('Mongo only pawn... in game of life.')\n",
			 f"\t\t\t'Mongo only pawn... in game of life.'\n\n",
			 f"\t\t\t>>> msg.output(message = “Without followers, evil cannot spread.”)\n",
			 f"\t\t\t'Without followers, evil cannot spread.'\n",
			 f"\t\t'''\n",
			 f"\t\tif Messenger.__printIt is not None:\n",
			 f"\t\t\tMessenger.__printIt(message)\n\n"]
	outFile.writelines(oLine)

def writeMsgOutput(outFile: io.TextIOWrapper) -> None:
	oLine = [f"\tdef output(self, msgType: str = msgcon.LOGINFO, message: str | dict = \"\") -> None:\n",
			 f"\t\t'''\n",
			 f"\t\tThis is the ONLY safe way to\n",
			 f"\t\tprint to the screen and the Log file.\n\n",
			 f"\t\tArgs:\n",
			 f"\t\t\tmsgType (str) - The type of log message\n",
			 f"\t\t\tmessage (str) - The message to print.\n\n",
			 f"\t\tExamples:\n",
			 f"\t\t\t>>> msg.output(msgType = \"info\", \"Hello world!\")\n",
			 f"\t\t\t'Hello world!'\n\n",
			 f"\t\t\t>>> msg.output(message = \"Mongo only pawn... in game of life.\")\n",
			 f"\t\t\t'Mongo only pawn... in game of life.'\n\n",
			 f"\t\t\t>>> msg.output(msgType = \"warning\", message = \“Without followers, evil cannot spread.\”)\n",
			 f"\t\t\t'Without followers, evil cannot spread.'\n",
			 f"\t\t'''\n\n",
			 f"\t\tMessenger.outLog(self, msgType=msgType, message=message)\n",
			 f"\t\tMessenger.outPrint(self, message)\n\n"]
	outFile.writelines(oLine)

def writeMsgOut(outFile: io.TextIOWrapper) -> None:
	writeMsgOutLog(outFile)
	writeMsgOutPrint(outFile)
	writeMsgOutput(outFile)

def writeMsgYNwarning(outFile: io.TextIOWrapper) -> None:

	oLine = [f"\tdef YNwarning(self, outMsg: str, quest: str) -> str:\n",
			 f"\t\t'''\n",
			 f"\t\tPrints a warning message that asks the user to answer yes or no.\n\n",
			 f"\t\tParameters:\n",
			 f"\t\t\toutMsg (str) - The message to print to the screen.\n",
			 f"\t\t\tquest  (str) - The question to print to the screen.\n\n",
			 f"\t\tNOTES:\n",
			 f"\t\t\tThis ignores any configuration options, so:\n\n",
			 f"\t\t\t\tThe routine will always print to the screen using print()\n",
			 f"\t\t'''\n",
			 f"\t\tprint(outMsg)\n",
			 f"\t\tretval = \"\"\n",
			 f"\t\twhile retval != \"Y\" and retval != \"N\":\n",
			 "\t\t\tretval = input (f\"{quest} ([Y]/N): \").upper()\n",
			 f"\t\t\tif retval == \"\":\n",
			 f"\t\t\t\tretval = \"Y\"\n",
			 f"\t\treturn retval\n\n"]
	outFile.writelines(oLine)

def writeMsgClass(outFile: io.TextIOWrapper) -> None:
	oLine = [f"all = (\"msg\")\n\n",
			 f"class Messenger:\n"]
	outFile.writelines(oLine)
	writeMsgClassHead(outFile)
	writeMsgClassMain(outFile)
	writeMsgConfig(outFile)
	writeMsgOut(outFile)
	writeMsgYNwarning(outFile)

def writeMsgTail(outFile: io.TextIOWrapper) -> None:
	oLine = [f"msg = Messenger()\n"]
	outFile.writelines(oLine)

def writeMessage(msgFile: str) -> None:
	'''
	writeMain() writes the main.py file

	Parameters:

	msgFile (str) - The name of the Python code file to write
	'''
	with open(msgFile, "w") as outFile:
		writeMsgHeader(outFile)
		writeDunders(outFile)
		writeMsgClass(outFile)
		writeMsgTail(outFile)
