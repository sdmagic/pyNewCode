# <p style="text-align: center;">pyNewCode</p>

## Description:

This application preforms all the usual start-of-project tasks for a new project. It:

- Creates the project's directory structure
  - Creates a project directory (if we're not using the current directory)
    - All directories will be subdirectories off the project directory
  - Creates a configuration directory (for the project's config files)
  - Creates a logs directory (for the project's log files)
  - Creates a modules directory (for the project's modules and utilities)

---

## Syntax:
#### pyNewCode.exe:
```
pyNewCode.exe [path]

	Examples:
		pyNewCode C:\Users\user\Desktop\MyProject
		(will build the new in C:\Users\user\Desktop\myProject directory)
```
#### python pyNewCode.py:
```
python pyNewCode.py [path]

	Examples:
		python pyNewCode.py C:\Users\user\Desktop\MyProject
		(will build the new project in C:\Users\user\Desktop\MyProject directory)
```
In either case, path is optional.

If not specified, the current directory will be used.

---
