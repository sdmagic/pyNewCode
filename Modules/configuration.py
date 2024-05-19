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

	dirConfig  (str)  (default = "config")  Configuration directory
	dirLogs    (str)  (default = "logs")    Logs directory
	dirModules (str)  (default = "modules") Modules directory

	getters & setters:

	home       (str)  (default = ".")       Project's home directory
	options    (dict) (default = {})        All Configuration options
	project    (str)  (default = "")        Project name
		NOTE: There's a setter for project that sets home and project from one path string.

	'''

	__instance		= None
	__yamlFile: str = os.path.join(os.getcwd(), "pyNewCode.yaml")
	__options: dict = {}	# Config options (read from YAML file)
	__project: str	= ""	# Project name
	__home: str		= ""	# Home directory

	def __new__(cls):
		if Configuration.__instance is None:
			Configuration.__instance = super(Configuration, cls).__new__(cls)
			Configuration.readConfig()

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
	def dirConfig(self) -> str:
		return "config" if type(retval := Configuration.__options.get("directories", {}).get("config")) is not str else retval

	@property
	def dirLogs(self) -> str:
		return "logs" if type(retval := Configuration.__options.get("directories", {}).get("logs")) is not str else retval

	@property
	def dirModules(self) -> str:
		return "modules" if type(retval := Configuration.__options.get("directories", {}).get("modules")) is not str else retval

	####################################################
	# CLASS getters and setters:

	@property
	def home(self) -> str:
		return Configuration.__home

	@property
	def options(self) -> str:
		return Configuration.__options
		
	@property
	def project(self) -> str:
		return Configuration.__project

	@project.setter
	def project(self, path: str) -> None:
		Configuration.__home, Configuration.__project = os.path.split(path)
		if Configuration.__project == "":
			Configuration.__project = "MyProject"
		if Configuration.__home == "":
			Configuration.__home = os.getcwd()

cfg = Configuration()
