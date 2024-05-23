import argparse
import os
from modules.configuration import cfg
from modules.directories import createDirs

def parseCLI() -> None:
	'''
	parseCLI parses the command line arguments
	and sends the results to the Configuration class.
	'''

	parser = argparse.ArgumentParser(description='Generate a new Python project.')
	parser.add_argument('workPath', nargs='?', 
						default=os.getcwd(),
						help='Optional project with optional path.')
			
	cfg.dirApp     = os.path.dirname(os.path.realpath(__file__)) # Set cfg.dirApp
	cfg.dirWorking = parser.parse_args().workPath	# Send path to Configuration
	cfg.yamlFile   = os.path.join(cfg.dirApp, "pyNewCode.yaml")
	cfg.readConfig()

def main() -> None:
	os.system('cls')
	print(f"{"-" * 80}")

	parseCLI()

	print(f'Application directory: "{cfg.dirApp}"')
	print(f'            YAML file: "{cfg.yamlFile}"')
	print(f'    Project directory: "{cfg.dirWorking}"')
	print(f'   Generating project: "{cfg.project}"')
	print(f'    Modules directory: "{cfg.dirModules}"')

	createDirs()
	
	print(f"{"-" * 80}")

if __name__ == '__main__':
    main()