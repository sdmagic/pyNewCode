
# pyNewCode

- [pyNewCode](#pynewcode)
	- [Description:](#description)
	- [Syntax:](#syntax)
	- [Example Outputs](#example-outputs)
	- [Handy Newsletters](#handy-newsletters)

---

## Description:

This application preforms all the usual start-of-project tasks for a new project. It:

**NOTE:**

All writing is driven by the YAML configuration file -- If you don't want
the file or directory, you can just set that item to false.

- Creates the project's directory structure
  - Creates a project directory (if we're not using the current directory)
    - All directories will be subdirectories off the project directory
  - Creates a configuration directory (for the project's config files)
  - Creates a logs directory (for the project's log files)
  - Creates a modules directory (for the project's modules and utilities)

- Creates a Project's base files
  - Will warn and ask if a file already exists
  - Creates the project's main file (starup point)
  - Creates the project's configuration file
  - Creates the project's modules\\__init__.py file
  - Creates the project's YAML file
  - Creates a todo.txt file for the project
    - Please follow the instructions in this file after generation

---

## Syntax:

```
pyNewCode.exe [path]

	Examples:
		pyNewCode C:\Users\user\Desktop\MyProject
		(will build the new in C:\Users\user\Desktop\myProject directory)
```

OR

```
python pyNewCode.py [path]

	Examples:
		python pyNewCode.py C:\Users\user\Desktop\MyProject
		(will build the new project in C:\Users\user\Desktop\MyProject directory)
```
In either case, path is optional.

If not specified, the current directory will be used.

---

## Example Outputs

todo.txt file
```
# YAML file todos:
	- Change "author: Nobody" to your name
	- Change "project: MyNewProject" to your project name
```

project.yaml file
```
author: Nobody
directories:
  config: config
  logs: logs
  modules: modules
options:
  logVerbose: true
  logging: true
  screenclear: true
  screenpretty: true
  screenprint: true
project: MyNewProject
version: 0.0.1
```
---

## Handy Newsletters

* [Awesome Python List](https://python.libhunt.com/newsletter)
* [Data Science Simplified](https://mathdatasimplified.com/)
* [Dev Tips Weekly](https://ardalis.com/tips/)
* [Postgres Weekly](https://postgresweekly.com/)
* [Programming Digest](https://programmingdigest.net/)
* [PyCoder’s Weekly](https://pycoders.com/)
* [Python Morsels](https://www.pythonmorsels.com/newsletter/)
* [Python Weekly](https://www.pythonweekly.com/)
* [Real Python](https://realpython.com/newsletter/)
* [VSCode.email](https://vscode.email/)
