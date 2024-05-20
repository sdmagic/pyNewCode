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
	parser.add_argument('project', nargs='?', 
						default=os.path.join(os.getcwd(), "myProject"),
						help='Optional project with optional path.')

	cfg.project = parser.parse_args().project	# Parse project name & path

def main() -> None:
	os.system('cls')

	parseCLI()
	createDirs()

	print(f'Generating project: "{cfg.project}"')
	print(f'Project directory: "{cfg.home}"')
	
if __name__ == '__main__':
    main()