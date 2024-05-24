import datetime
import logging
import os
import modules.message as msgcon	# msgcon because we use __init__.py for the contstants
from modules.configuration import cfg
from modules.directories import buildDir
from rich.pretty import pprint

__author__: str		= "Stephen D. Cooper <sdmagic@gmail.com>"
__copyright__: str	= "Copyright 2024 by Stephen D. Cooper. All rights reserved."
__status__: str		= "alpha"
__version__: str	= "0.0.1"
__date__: str		= "2024-05-23"	# YYYY-MM-DD

__all__ = ("msg")

class Messenger:
	'''
	Messenger is a singleton class -- Only one per application

	Tests whether to print to the screen using pprint() or print()
	After instantiation, the class will set the _printIt variable to either
	or None, depending on the user's configuration settings.
	
	Use Messenger.output() to print to the screen.

	DO NOT USE _printIt directly. Use Messenger.output() instead.

	Private Attributes:
		__instance (class)	- Singleton instance
		_printIt (function) - The function to use to print to the screen.

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
		logFname: str = os.path.join(cfg.dirLogs, 
						f'log{datetime.datetime.now().strftime("%Y%m%d")}.log')
		logFormat: str = '%(asctime)s (%(levelname)s) %(message)s'

		if cfg.logging:
			print(f"Logging to: {logFname}")
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

		print(f"Printing to screen: {Messenger.__printIt}")

	def output(self, msgType: str = "info", message: str | dict = "") -> None:
		'''
		This is the ONLY safe way to
		print to the screen and the logs
			
		Args:
			msgType (str) - The type of log message
			message (str) - The message to print.

		Examples:
			>>> msg.Output(msgType = "info", "Hello world!")
			'Hello world!'

			>>> msg.Output(message = "Mongo only pawn... in game of life.")
			'Mongo only pawn... in game of life.'

			>>> msg.Output(msgType = "warning", message = “Without followers, evil cannot spread.”)
			'Without followers, evil cannot spread.'
		'''
		
		if cfg.logging:
			if type(message) == str:
				match msgType.lower():
					case msgcon.LOGCRITICAL:
						logging.critical(message)
					case msgcon.LOGDEBUG:
						logging.debug(message)
					case msgcon.LOGERROR:
						logging.error(message)
					case msgcon.LOGINFO:
						logging.info(message)
					case msgcon.LOGNOLOG:	# Our own log type -- Don't log
						pass
					case msgcon.LOGWARNING:
						logging.warning(message)
					case _:
						logging.error("Unknown message")

		if self._printIt is not None:
			self._printIt(message)

'''
msg is our singleton instance of the Messenger class
'''
msg = Messenger()
