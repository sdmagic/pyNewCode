import argparse
import os
from modules.configuration import cfg
from modules.directories import createDirs
from modules.message import msg

def initialzeConfiguration(workPath: str) -> None:
	'''
	Initialize the Configuration class.

	Specifically, set the working and app directories and
	yaml file.

	Then, read the yaml file into the Configuration class.
	'''
	cfg.dirApp     = os.path.dirname(os.path.realpath(__file__)) # Set Application directory
	cfg.dirWorking = workPath	# Set working directory in Configuration
	cfg.yamlFile   = os.path.join(cfg.dirApp, "pyNewCode.yaml")

	# Paths are set -- Read the configuration file
	# This completes the initialization of the Configuration class
	cfg.readConfig()

def parseCLI() -> str:
	'''
	parseCLI parses and returns the command line arguments.
	'''
	parser = argparse.ArgumentParser(description='Generate a new Python project.')
	parser.add_argument('workPath', nargs='?', 
						default=os.getcwd(),
						help='Optional project with optional path.')

	return parser.parse_args().workPath

def main() -> None:
	os.system('cls')
	print(f"{"-" * 80}")

	initialzeConfiguration(parseCLI())

	createDirs()
	msg.config()

	print(f'Application directory: "{cfg.dirApp}"')
	print(f'            YAML file: "{cfg.yamlFile}"')
	print(f'    Project directory: "{cfg.dirWorking}"')
	print(f'   Generating project: "{cfg.project}"')
	print(f'    Modules directory: "{cfg.dirModules}"')
	
	print(f"{"-" * 80}")

if __name__ == '__main__':
    main()