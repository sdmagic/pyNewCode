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

all = ("writeYAML")

def writeYAML(yamlFile: str) -> None:
	'''
	writeYAML() writes the project.yaml file
	'''
	data = {'project': 'MyNewProject',
			'version': 'VersionNumber',
			'author': 'Nobody',
			'directories': {'config': 'config',
							'logs': 'logs',
							'modules':'modules'},
			'options': {'logging': True, 
						'logVerbose': True,
						'screenclear': True,
						'screenpretty': True,
						'screenprint': True}
	}

	with open(yamlFile, 'w') as outFile:
		yaml.dump(data, outFile, default_flow_style=False)
