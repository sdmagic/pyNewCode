'''
The application's main entry point.
'''

import os
from modules.configuration import cfg

__author__:    str = "Stephen D. Cooper"
__copyright__: str = "Copyright 2024 by Stephen D. Cooper. All rights reserved."
__version__:   str = "0.0.1"
__date__:      str = "2024-05-26"	# YYYY-MM-DD

def initialzeConfiguration() -> None:
	'''
	Initialize the Configuration class.
	Specifically, set the working and app directories and
	yaml file.
	Then, read the yaml file into the Configuration class.
	'''
	cfg.dirApp     = os.path.dirname(os.path.realpath(__file__)) # Set Application directory
	cfg.dirWorking = os.getcwd()	# Set working directory in Configuration
	cfg.yamlFile   = os.path.join(cfg.dirApp, f'MyNewProject.yaml')

	# Paths are set -- Read the configuration file
	# This completes the initialization of the Configuration class
	cfg.readConfig()

def main():
	initialzeConfiguration()

if __name__ == '__main__':
	main()
