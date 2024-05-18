import argparse
import os
from modules.configuration import cfg

def main() -> None:
	# os.system('cls')

	parser = argparse.ArgumentParser(description='Generate a new Python project.')
	# parser.add_argument('-p, --project', type=str, help='Name of the project.')
	# parser.add_argument('project', type=str, help='Name of the project.', required=False)
	parser.add_argument('project', nargs='?', 
						default=os.path.join(os.getcwd(), "myProject"),
						help='Optional project with optional path.')

	print(f"--'{parser.parse_args().project}'--")
	print(f"--'{type(parser.parse_args().project)}'--")
	cfg.project = parser.parse_args().project	# Parse project name & path

	print(f'Generating project: "{cfg.project}"')
	print(f'Project directory: "{cfg.home}"')
	
if __name__ == '__main__':
    main()