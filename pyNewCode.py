import argparse
import os
import modules.constants as msgcon
from modules.configuration import cfg
from modules.directories import createDirs
from modules.message import msg
from modules.write import writeFiles

def initialzeConfiguration(workPath: str) -> None:
	'''
	Initialize the Configuration class.

	Specifically, set the working and app directories and
	yaml file.

	The working directory (project app directory) is passed in
	because it's built if the user didn't give one on the command
	line -- Command line processing is handled elsewhere.

	We find our application path here, in the 
	application's entry-point file instead of in 
	the Configuration class file because __file__ 
	is the current file and configuration.py lives 
	in our modules directory which is not the application path.

	We could build the YAML filename in the Configuration class, 
	but we do it here and pass it to the Configuration class so 
	that the Configuration class stays dumb and can be used in 
	other applications. Also, our application name is reliant on 
	being the first to use the name in PyPI and Anaconda 
	libraries. Since we want the YAML file to carry our 
	application name, we build it here for these reasons.

	Finally, we tell the Configuration class to read the yaml 
	file. This configures the Configuration class.
	'''

	cfg.dirWorking = workPath
	cfg.dirApp     = os.path.dirname(os.path.realpath(__file__))
	cfg.fileYAML   = os.path.join(cfg.dirApp, "pyNewCode.yaml")

	cfg.readConfig()

def parseCLI() -> str:
	'''
	parseCLI parses and returns the command line arguments.
	In the case of this application, there is only one possible
	command line argument -- The project's main directory.

	Our working path (the project's main directory) is either
	where we are when the application was started, or a path
	that's given on the command line.
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
	msg.output(message = f'            YAML file: "{cfg.fileYAML}"')
	msg.output(message = f'    Project directory: "{cfg.dirWorking}"')
	msg.output(message = f'   Generating project: "{cfg.project}"')
	msg.output(message = f'    Modules directory: "{cfg.dirModules}"')
	msg.output(message = f'    Project Main File: "{os.path.join(cfg.dirWorking, f"{cfg.project}.py")}"')

	writeFiles()

	msg.output(message = cfg.options)
	
	print(f"{"-" * 80}")

if __name__ == '__main__':
    main()
	