import os
import yaml
import modules.constants as msgcon
from modules.configuration import cfg
from modules.message import msg

__author__: str		= "Stephen D. Cooper <sdmagic@gmail.com>"
__copyright__: str	= "Copyright 2024 by Stephen D. Cooper. All rights reserved."
__status__: str		= "alpha"
__version__: str	= "0.0.1"
__date__: str		= "2024-05-26"	# YYYY-MM-DD

all = ("writeTodo")

def writeTodo(todoFile: str) -> None:
	'''
	writeToDo() writes the project's todo.txt file
	'''

	with open(todoFile, 'w') as outFile:
		oLine = [f"# {cfg.project} Todos\n\n",
				 f"## YAML file todos\n\n",
				 f"[ ] Change author: \"Nobody\" to your name\n\n",
				 f"[ ] Change project: \"MyNewProject\" to your project name\n\n",
				 f"[ ] Change version: \"VersionNumber\" to your version number\n"]

		outFile.writelines(oLine)

