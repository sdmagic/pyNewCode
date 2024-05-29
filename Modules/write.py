import io
import os
import modules as msgcon	# msgcon because we use msg for the class
from datetime import date, datetime
from modules.configuration import cfg
from modules.message import msg
from modules.writeConfig import writeConfig
from modules.writeInit import writeInit
from modules.writeMain import writeMain
from modules.writeTodo import writeTodo
from modules.writeYAML import writeYAML

__author__: str		= "Stephen D. Cooper <sdmagic@gmail.com>"
__copyright__: str	= "Copyright 2024 by Stephen D. Cooper. All rights reserved."
__status__: str		= "alpha"
__version__: str	= "0.0.1"
__date__: str		= "2024-05-07"	# YYYY-MM-DD

all = ("writeFiles")


def writeCheckForExistence(fName: str) -> bool:
	'''
	writeCheckForExistence() Checks for the file's existence 
									and asks for confirmation
	'''
	retval = "Y"

	if os.path.exists(fName):
		retval = msg.YNwarning(f'"{fName}" exists!', f'Continue and overwrite')

	if retval != "Y":
		msg.output(msgType = msgcon.LOGWARNING, message = f'     Skipping File: "{fName}"')
	else:
		msg.output(message = f'         Writing File: "{fName}"')

	return retval == "Y"

def writeFiles() -> None:
	'''
	writeFiles() - Write the files for the project.
	'''
	homeDir = os.getcwd()
	
	if cfg.buildMain:
		mainFile = os.path.join(cfg.dirWorking, f"{cfg.project}.py")
		if writeCheckForExistence(mainFile):
			writeMain(mainFile)

	if cfg.buildConfig:
		# cfgFile = os.path.join(cfg.dirWorking, cfg.dirModules, f"YADAconfiguration.py")
		cfgFile = os.path.join(cfg.dirWorking, cfg.dirModules, f"configuration.py")
		if writeCheckForExistence(cfgFile):
			writeConfig(cfgFile)

	if cfg.buildInit:
		# initFile = os.path.join(cfg.dirWorking, cfg.dirModules, f"YADA__init__.py")
		initFile = os.path.join(cfg.dirWorking, cfg.dirModules, f"__init__.py")
		if writeCheckForExistence(initFile):
			writeInit(initFile)

	if cfg.buildYAML:
		yamlFile = os.path.join(cfg.dirWorking, f"{cfg.project}.yaml")
		if writeCheckForExistence(yamlFile):
			writeYAML(yamlFile)

	if cfg.buildTodo:
		# todoFile = os.path.join(cfg.dirWorking, f"YADAtodo.md")
		todoFile = os.path.join(cfg.dirWorking, f"todo.md")
		if writeCheckForExistence(todoFile):
			writeTodo(todoFile)

	os.chdir(homeDir)