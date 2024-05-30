import datetime
import logging
import os
# import modules.message as msgcon	# msgcon because we use __init__.py for the contstants
from modules.configuration import cfg
from modules.directories import buildDir
from rich.pretty import pprint

__author__: str		= "Stephen D. Cooper <sdmagic@gmail.com>"
__copyright__: str	= "Copyright 2024 by Stephen D. Cooper. All rights reserved."
__status__: str		= "alpha"
__version__: str	= "0.0.1"
__date__: str		= "2024-05-23"	# YYYY-MM-DD

__all__ = ("msg")

LOGCRITICAL:	str	= "critical"
LOGDEBUG:		str	= "debug"
LOGERROR:		str	= "error"
LOGINFO:		str	= "info"
LOGNOLOG:		str	= "nolog"
LOGWARNING:		str	= "warning"

class Messenger:
	'''
	Messenger is a singleton class -- Only one per application

	Tests whether to print to the screen using pprint() or print()
	After instantiation, the class will set the _printIt variable to either
	or None, depending on the user's configuration settings.
	
	Use Messenger.output() to print to the screen.

	NOTES:

		DO NOT USE __printIt directly. Use Messenger.output()
	
		message.py REQUIRES a cfg object that has these properties:

			cfg.dirApp       (str)  - Application directory
			cfg.dirLogs      (str)  - Log file directory
			cfg.logging      (bool) - Log messages?
			cfg.screenPretty (bool) - Use pprint()?
			cfg.screenPrint  (bool) - Prin to screen?

	Private Attributes:

		__instance (class)	 - Singleton instance
		__printIt (function) - The function to use to print to the screen.

	Methods:

		output(msg) - Prints the message to the screen and log file.
	'''

	__instance = None	# Singleton instance
	__printIt  = None	# Function that prints to the screen

	def __new__(cls):
		if Messenger.__instance is None:
			Messenger.__instance = super(Messenger, cls).__new__(cls)

		return Messenger.__instance

	@classmethod
	def config(cls) -> None:
		Messenger.configPrintFunction()
		Messenger.configLogs()

	@classmethod
	def configLogs(cls) -> None:
		'''
		configLogs() configures the logging system.
		'''
		# ** Stupid Programmer Tricks to make the editor easier to use
		# 		** These are long lines, so we use variables
		# 		** to shorten the call to logging.basicConfig()
		logFname: str = os.path.join(cfg.dirApp, cfg.dirLogs, 
						f'log{datetime.datetime.now().strftime("%Y%m%d")}.log')
		logFormat: str = '%(asctime)s (%(levelname)s) %(message)s'

		if cfg.logging:
			logging.basicConfig(level=logging.DEBUG,
								filename=logFname,
								encoding='utf-8',
								filemode='a',
								format=logFormat,
								datefmt='%Y-%m-%d %H:%M:%S')

	@classmethod
	def configPrintFunction(cls) -> None:
		'''
		configPrintFunction() configures the print function.
		'''
		if cfg.screenPretty:
			Messenger.__printIt: function = pprint
		elif cfg.screenPrint:
			Messenger.__printIt: function = print
		else:
			Messenger.__printIt: NoneType = None

	def outLog(self, msgType: str = LOGINFO, message: str | dict = "") -> None:
		'''
		This is the ONLY safe way to
		print to the Log file.
			
		Args:
			msgType (str) - The type of log message
			message (str) - The message to print.

		Examples:
			>>> msg.outLog(msgType = "info", "Hello world!")
			'Hello world!'

			>>> msg.outLog(message = "Mongo only pawn... in game of life.")
			'Mongo only pawn... in game of life.'

			>>> msg.outLog(msgType = "warning", message = “Without followers, evil cannot spread.”)
			'Without followers, evil cannot spread.'
		'''
		if cfg.logging:
			if type(message) == str:
				msgType = msgType.lower()
				if msgType == LOGCRITICAL:
					logging.critical(message)
				elif msgType == LOGDEBUG:
					logging.debug(message)
				elif msgType == LOGERROR:
					logging.error(message)
				elif msgType == LOGINFO:
					logging.info(message)
				elif msgType == LOGNOLOG:	# Our own log type -- Don't log
					pass
				elif msgType == LOGWARNING:
					logging.warning(message)
				else:
					logging.error("Unknown message")

	def outPrint(self, message: str | dict = "") -> None:
		'''
		This is the ONLY safe way to print to the screen.
			
		Args:
			message (str) - The message to print.

		Examples:
			>>> msg.output("Hello world!")
			'Hello world!'

			>>> msg.output("Mongo only pawn... in game of life.")
			'Mongo only pawn... in game of life.'

			>>> msg.output(message = “Without followers, evil cannot spread.”)
			'Without followers, evil cannot spread.'
		'''
		if Messenger.__printIt is not None:						
			Messenger.__printIt(message)

	def output(self, msgType: str = LOGINFO, message: str | dict = "") -> None:
		'''
		This is the ONLY safe way to
		print to the screen and the Log file.
			
		Args:
			msgType (str) - The type of log message
			message (str) - The message to print.

		Examples:
			>>> msg.output(msgType = "info", "Hello world!")
			'Hello world!'

			>>> msg.output(message = "Mongo only pawn... in game of life.")
			'Mongo only pawn... in game of life.'

			>>> msg.output(msgType = "warning", message = “Without followers, evil cannot spread.”)
			'Without followers, evil cannot spread.'
		'''
		Messenger.outLog(self, msgType=msgType, message=message)
		Messenger.outPrint(self, message)

	def YNwarning(self, outMsg: str, inMsg: str) -> str:
		'''
		Prints a warning message that asks the user to answer yes or no.

		NOTES:
			This ignores any configuration options, so:

				The routine will always print to the screen using print()
		'''
		print(outMsg)
		retval = ""
		while retval != "Y" and retval != "N":
			retval = input (f"{inMsg} ([Y]/N): ").upper()
			if retval == "":
				retval = "Y"
		return retval


'''
msg is our singleton instance of the Messenger class
'''
msg = Messenger()
