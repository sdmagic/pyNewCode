'''
The application's configuration program file.
'''

import io
import os
import yaml						# https://pypi.org/project/PyYAML/
from datetime import date, datetime

__author__:    str = "Stephen D. Cooper"
__copyright__: str = "Copyright 2024 by Stephen D. Cooper. All rights reserved."
__version__:   str = "0.0.1"
__date__:      str = "2024-05-26"	# YYYY-MM-DD

all = ("cfg")

class Configuration:
	'''
	Configuration is a singleton class
	Only one per application

	Reads a configuration file and 
	provides options to the application.

	properties:

	author       (default = "Nobody")     The project's author 
	dirConfig    (default = "config")     The project's configuration directory
	dirLogs      (default = "logs")       The project's logs directory
	dirModules   (default = "modules")    The project's modules directory
	logging      (default = True)           Are we logging?
	logVerbose   (default = True)           Are we verbose logging?
	options      (default = )               Configuration options as dictionary
	project      (default = "newProject") Project name
	screenClear  (default = True)           Does our project clear the screen?
	screenPretty (default = True)           Do we use pprint() for printing?
	screenPrint  (default = True)           Do we print at all?
	version      (default = "0.0.0")      The Project's version number
	dirApp       (default = ".")          The project's Application startup directory
	dirWorking   (default = ".")          The project's working directory
	yamlFile     (default = ".\newProject.yaml") The Project's YAML file
	'''

	__instance		= None	# The singleton instance
	__yamlFile: str = os.path.join(os.getcwd(), 'config.yaml')
	__options: dict = {}	# Config options (read from YAML file)

	def __new__(cls):
		if Configuration.__instance is None:
			Configuration.__instance = super(Configuration, cls).__new__(cls)

		return Configuration.__instance

	@classmethod
	def readConfig(cls) -> None:
		'''
		readConfig() reads our settings & options YAML file
		We first check to see if the YAML file exists.
		If it does, read it. Otherwise, all 
		properties will return default values.

		..note::

			Applications _only_ need to call this 
			this method IF the YAML configuration
			file has changed during the app's life
		'''
		if os.path.exists(Configuration.__yamlFile):
			with open(Configuration.__yamlFile, "r") as ymlfile:
				Configuration.__options = yaml.safe_load(ymlfile)

	####################################################
	# CLASS PROPERTIES (application settings & options):

	@property
	def author(self) -> str:
		return 'Nobody' if type(retval := Configuration.__options.get('author')) is not str else retval

	@property
	def dirConfig(self) -> str:
		return 'config' if type(retval := Configuration.__options.get('directories', {}).get('config')) is not str else retval

	@property
	def dirLogs(self) -> str:
		return 'logs' if type(retval := Configuration.__options.get('directories', {}).get('logs')) is not str else retval

	@property
	def dirModules(self) -> str:
		return 'modules' if type(retval := Configuration.__options.get('directories', {}).get('modules')) is not str else retval

	@property
	def logging(self) -> str:
		return False if type(retval := Configuration.__options.get('options', {}).get('logging')) is not bool else retval

	@property
	def logVerbose(self) -> str:
		return False if type(retval := Configuration.__options.get('options', {}).get('logverbose')) is not bool else retval

	@property
	def options(self) -> dict:
		return Configuration.__options

	@property
	def project(self) -> str:
		return 'main.py' if type(retval := Configuration.__options.get('project')) is not str else retval

	@property
	def screenClear(self) -> bool:
		return True if type(retval := Configuration.__options.get('options', {}).get('screenclear')) is not bool else retval

	@property
	def screenPretty(self) -> bool:
		return False if type(retval := Configuration.__options.get('options', {}).get('screenpretty')) is not bool else retval

	@property
	def screenPrint(self) -> bool:
		return False if type(retval := Configuration.__options.get('options', {}).get('screenprint')) is not bool else retval

	@property
	def version(self) -> str:
		return 'alpha' if type(retval := Configuration.__options.get('version')) is not str else retval

	####################################################
	# CLASS getters and setters:

	@property
	def dirApp(self) -> str:
		return Configuration.__dirApp

	@dirApp.setter
	def dirApp(self, path: str) -> None:
		Configuration.__dirApp = path

	@property
	def dirWorking(self) -> str:
		return Configuration.__dirWorking

	@dirWorking.setter
	def dirWorking(self, path: str) -> None:
		Configuration.__dirWorking = path

	@property
	def yamlFile(self) -> str:
		return Configuration.__yamlFile

	@yamlFile.setter
	def yamlFile(self, yamlPath: str) -> None:
		Configuration.__yamlFile = yamlPath

cfg = Configuration()
