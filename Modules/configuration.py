from argparse import Namespace
import os
import yaml						# https://pypi.org/project/PyYAML/

__author__: str		= "Stephen D. Cooper <sdmagic@gmail.com>"
__copyright__: str	= "Copyright 2024 by Stephen D. Cooper. All rights reserved."
__status__: str		= "alpha"
__version__: str	= "0.0.1"
__date__: str		= "2024-05-07"	# YYYY-MM-DD

all = ("cfg")

class Configuration:
	'''
	Configuration is a singleton class
	Only one per application

	Reads a configuration file and 
	provides options to the application.

	properties:

	author       (str)  (default = "No Author Given) Project Author's name
	buildConfig  (str)  (default = True)             Build the project's Configuration file?
	buildInit    (str)  (default = True)             Build the project's modules __init__.py file?
	buildMain    (str)  (default = True)             Build the project's main file?
	dirConfig    (str)  (default = "config")         Configuration directory
	dirLogs      (str)  (default = "logs")           Logs directory
	dirModules   (str)  (default = "modules")        Modules directory
	logging      (bool) (default = True)             Are we logging?
	project      (str)  (default = "newProject")     Project name
	screenPretty (bool) (default = True)             Are we using pprint()?
	screenPrint  (bool) (default = True)             Are we using printing to the screen?
	version      (str)  (default = "0.0.0")          Project version

	getters & setters:

	dirApp     (str)  (default = ".")       Project's home directory
	dirWorking (str)  (default = ".\\")     Project's working directory
		NOTE: There's a setter for dirWorking that sets it from a given path
	options    (dict) (default = {})        All Configuration options

	'''

	__instance		  = None
	__yamlFile: str   = os.path.join(os.getcwd(), "pyNewCode.yaml")
	__options: dict   = {}	  # Config options (read from YAML file)
	__dirApp: str     = ""	  # Application's starting directory
	__dirWorking: str = ".\\" # Home directory

	def __new__(cls):
		if Configuration.__instance is None:
			Configuration.__instance = super(Configuration, cls).__new__(cls)

		return Configuration.__instance

	@classmethod
	def readConfig(cls) -> None:
		'''
		readConfig() reads our settings & options YAML file

		We first check to see if the YAML file exists.
		If it does, read it, otherwise, don't and
		all properties will return default values.

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
		return "No Author Given" if type(retval := Configuration.__options.get("author")) is not str else retval

	@property
	def buildConfig(self) -> str:
		return True if type(retval := Configuration.__options.get("build", {}).get("config")) is not bool else retval

	@property
	def buildInit(self) -> str:
		return True if type(retval := Configuration.__options.get("build", {}).get("init")) is not bool else retval

	@property
	def buildMain(self) -> str:
		return True if type(retval := Configuration.__options.get("build", {}).get("main")) is not bool else retval

	@property
	def dirConfig(self) -> str:
		return "config" if type(retval := Configuration.__options.get("directories", {}).get("config")) is not str else retval

	@property
	def dirLogs(self) -> str:
		return "logs" if type(retval := Configuration.__options.get("directories", {}).get("logs")) is not str else retval

	@property
	def dirModules(self) -> str:
		return "modules" if type(retval := Configuration.__options.get("directories", {}).get("modules")) is not str else retval

	@property
	def logging(self) -> str:
		return True if type(retval := Configuration.__options.get("opions", {}).get("logging")) is not bool else retval

	@property
	def options(self) -> str:
		return Configuration.__options

	@property
	def project(self) -> str:
		return "newProject" if type(retval := Configuration.__options.get("project")) is not str else retval

	@property
	def screenPretty(self) -> str:
		return True if type(retval := Configuration.__options.get("opions", {}).get("screenpretty")) is not bool else retval

	@property
	def screenPrint(self) -> str:
		return True if type(retval := Configuration.__options.get("opions", {}).get("screenprint")) is not bool else retval

	@property
	def version(self) -> str:
		return "0.0.0" if type(retval := Configuration.__options.get("version")) is not str else retval

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
