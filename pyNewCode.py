import argparse
import os
from modules.configuration import cfg
from modules.directories import createDirs
from modules.message import msg
from modules.write import writeFiles

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
	parseCLI parses and returns the comma
	nd line arguments.
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

	msg.output(message = f'{"-" * 80}')
	msg.output(message = f'     Building Project: "{cfg.project}"')
	msg.output(message = f'Application directory: "{cfg.dirApp}"')
	msg.output(message = f'            YAML file: "{cfg.yamlFile}"')
	msg.output(message = f'    Project directory: "{cfg.dirWorking}"')
	msg.output(message = f'   Generating project: "{cfg.project}"')
	msg.output(message = f'    Modules directory: "{cfg.dirModules}"')
	msg.output(message = f'    Project Main File: "{os.path.join(cfg.dirWorking, f"{cfg.project}.py")}"')

	writeFiles()

	msg.output(message = cfg.options)
	
	print(f"{"-" * 80}")

	# TODO: Check for existing files
	# ----- We do not want to overwrite existing files

	# retval = msg.YNwarning("File exists", "Proceed and overwrite?")
	# msg.output(message = f"You selected: \"{retval}\"")

if __name__ == '__main__':
    main()
	