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
__date__: str		= "2024-05-07"	# YYYY-MM-DD

all = ("writeConfig")

def writeConfigHeader(outFile: io.TextIOWrapper) -> None:
	'''
	writeConfigHeader() - Write the config header to the file.
	'''
	oLine = [f"'''\n",
			 f"The application's configuration program file.\n",
			 f"'''\n\n",
			 f"import io\n",
			 f"import os\n",
			 f"import yaml						# https://pypi.org/project/PyYAML/\n",
			 f"from datetime import date, datetime\n\n"]
	outFile.writelines(oLine)

def writeConfigTail(outFile: io.TextIOWrapper) -> None:
	oLine = [f"cfg = Configuration()\n"]
	outFile.writelines(oLine)

def writeConfigClassHead(outFile: io.TextIOWrapper) -> None:
	oLine = [f"\t'''\n",
			 f"\tConfiguration is a singleton class\n",
			 f"\tOnly one per application\n\n",
			 f"\tReads a configuration file and \n",
			 f"\tprovides options to the application.\n\n",
			 f"\tproperties:\n\n",
			 f"\tauthor       (default = \"Nobody\")     The project's author \n",
			 f"\tdirConfig    (default = \"config\")     The project's configuration directory\n",
			 f"\tdirLogs      (default = \"logs\")       The project's logs directory\n",
			 f"\tdirModules   (default = \"modules\")    The project's modules directory\n",
			 f"\tlogging      (default = True)           Are we logging?\n",
			 f"\tlogVerbose   (default = True)           Are we verbose logging?\n",
			 f"\toptions      (default = )               Configuration options as dictionary\n",
			 f"\tproject      (default = \"newProject\") Project name\n",
			 f"\tscreenClear  (default = True)           Does our project clear the screen?\n",
			 f"\tscreenPretty (default = True)           Do we use pprint() for printing?\n",
			 f"\tscreenPrint  (default = True)           Do we print at all?\n",
			 f"\tversion      (default = \"0.0.0\")      The Project's version number\n",
			 f"\tdirApp       (default = \".\")          The project's Application startup directory\n",
			 f"\tdirWorking   (default = \".\")          The project's working directory\n",
			 f"\tyamlFile     (default = \"newProject.yaml\") The Project's YAML file\n",
			 f"\t'''\n\n"]
	outFile.writelines(oLine)

def writeConfigNew(outFile: io.TextIOWrapper) -> None:
	oLine = [f"\tdef __new__(cls):\n",
			 f"\t\tif Configuration.__instance is None:\n",
			 f"\t\t\tConfiguration.__instance = super(Configuration, cls).__new__(cls)\n\n",
			 f"\t\treturn Configuration.__instance\n\n"]
	outFile.writelines(oLine)

def writeConfigYAML(outFile: io.TextIOWrapper) -> None:

	oLine = [f"\t@classmethod\n",
			 f"\tdef readConfig(cls) -> None:\n",
			 f"\t\t'''\n",
			 f"\t\treadConfig() reads our settings & options YAML file\n",

			 f"\t\tWe first check to see if the YAML file exists.\n",
			 f"\t\tIf it does, read it. Otherwise, all \n",
			 f"\t\tproperties will return default values.\n\n",

			 f"\t\t..note::\n\n",

			 f"\t\t\tApplications _only_ need to call this \n",
			 f"\t\t\tthis method IF the YAML configuration\n",
			 f"\t\t\tfile has changed during the app's life\n",
			 f"\t\t'''\n",
			 f"\t\tif os.path.exists(Configuration.__yamlFile):\n",
			 f"\t\t\twith open(Configuration.__yamlFile, \"r\") as ymlfile:\n",
			 f"\t\t\t\tConfiguration.__options = yaml.safe_load(ymlfile)\n\n"]
	outFile.writelines(oLine)

def writeConfigProperties(outFile: io.TextIOWrapper) -> None:
	
	oLine = [f"\t####################################################\n",
			 f"\t# CLASS PROPERTIES (application settings & options):\n\n",
			 f"\t@property\n",
			 f"\tdef author(self) -> str:\n",
			 f"\t\treturn 'Nobody' if type(retval := Configuration.__options.get('author')) is not str else retval\n\n",
			 f"\t@property\n",
			 f"\tdef dirConfig(self) -> str:\n",
			 f"\t\treturn 'config' if type(retval := Configuration.__options.get('directories', {{}}).get('config')) is not str else retval\n\n"]
	outFile.writelines(oLine)

	oLine = [f"\t@property\n",
			 f"\tdef dirLogs(self) -> str:\n",
			 f"\t\treturn 'logs' if type(retval := Configuration.__options.get('directories', {{}}).get('logs')) is not str else retval\n\n",
			 f"\t@property\n",
			 f"\tdef dirModules(self) -> str:\n",
			 f"\t\treturn 'modules' if type(retval := Configuration.__options.get('directories', {{}}).get('modules')) is not str else retval\n\n"]
	outFile.writelines(oLine)


	oLine = [f"\t@property\n",
			 f"\tdef logging(self) -> str:\n",
			 f"\t\treturn False if type(retval := Configuration.__options.get('options', {{}}).get('logging')) is not bool else retval\n\n",
			 f"\t@property\n",
			 f"\tdef logVerbose(self) -> str:\n",
			 f"\t\treturn False if type(retval := Configuration.__options.get('options', {{}}).get('logverbose')) is not bool else retval\n\n",
			 f"\t@property\n",
			 f"\tdef options(self) -> dict:\n",
			 f"\t\treturn Configuration.__options\n\n",
			 f"\t@property\n",
			 f"\tdef project(self) -> str:\n",
			 f"\t\treturn 'main.py' if type(retval := Configuration.__options.get('project')) is not str else retval\n\n"]
	outFile.writelines(oLine)

	oLine = [f"\t@property\n",
			 f"\tdef screenClear(self) -> bool:\n",
			 f"\t\treturn True if type(retval := Configuration.__options.get('options', {{}}).get('screenclear')) is not bool else retval\n\n",
			 f"\t@property\n",
			 f"\tdef screenPretty(self) -> bool:\n",
			 f"\t\treturn False if type(retval := Configuration.__options.get('options', {{}}).get('screenpretty')) is not bool else retval\n\n",
			 f"\t@property\n",
			 f"\tdef screenPrint(self) -> bool:\n",
			 f"\t\treturn False if type(retval := Configuration.__options.get('options', {{}}).get('screenprint')) is not bool else retval\n\n"]
	outFile.writelines(oLine)

	oLine = [f"\t@property\n",
			 f"\tdef version(self) -> str:\n",
			 f"\t\treturn 'alpha' if type(retval := Configuration.__options.get('version')) is not str else retval\n\n"]

	outFile.writelines(oLine)

def writeConfigGettersSetters(outFile: io.TextIOWrapper) -> None:

	oLine = [f"\t####################################################\n",
			 f"\t# CLASS getters and setters:\n\n",

			 f"\t@property\n",
			 f"\tdef dirApp(self) -> str:\n",
			 f"\t\treturn Configuration.__dirApp\n\n",

			 f"\t@dirApp.setter\n",
			 f"\tdef dirApp(self, path: str) -> None:\n",
			 f"\t\tConfiguration.__dirApp = path\n\n",

			 f"\t@property\n",
			 f"\tdef dirWorking(self) -> str:\n",
			 f"\t	return Configuration.__dirWorking\n\n",

			 f"\t@dirWorking.setter\n",
			 f"\tdef dirWorking(self, path: str) -> None:\n",
			 f"\t	Configuration.__dirWorking = path\n\n",

			 f"\t@property\n",
			 f"\tdef yamlFile(self) -> str:\n",
			 f"\t	return Configuration.__yamlFile\n\n",

			 f"\t@yamlFile.setter\n",
			 f"\tdef yamlFile(self, yamlPath: str) -> None:\n",
			 f"\t	Configuration.__yamlFile = yamlPath\n\n"]

	outFile.writelines(oLine)

def writeConfigClassMain(outFile: io.TextIOWrapper) -> None:
	oLine = [f"\t__instance		= None\t# The singleton instance\n",	
			 f"\t__yamlFile: str = os.path.join(os.getcwd(), 'config.yaml')\n",
			 f"\t__options: dict = {{}}\t# Config options (read from YAML file)\n\n"]
	outFile.writelines(oLine)
	writeConfigNew(outFile)

def writeConfigClass(outFile: io.TextIOWrapper) -> None:
	oLine = [f"all = (\"cfg\")\n\n",
			 f"class Configuration:\n"]
	outFile.writelines(oLine)
	writeConfigClassHead(outFile)
	writeConfigClassMain(outFile)
	writeConfigYAML(outFile)
	writeConfigProperties(outFile)
	writeConfigGettersSetters(outFile)

def writeConfig(cfgFile: str) -> None:
	'''
	writeMain() writes the main.py file
	'''
	with open(cfgFile, "w") as outFile:
		writeConfigHeader(outFile)
		writeDunders(outFile)
		writeConfigClass(outFile)
		writeConfigTail(outFile)
