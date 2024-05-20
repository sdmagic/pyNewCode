# <p style="text-align: center;">pyNewCode</p>

---

## Description:

This application preforms all the usual start of project tasks for a new project. It:

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
pyNewCode.exe [[path]project]

	Examples:
		pyNewCode C:\Users\user\Desktop\MyProject
		(will build MyProject in the C:\Users\user\Desktop directory)
```
#### python pyNewCode.py:
```
python pyNewCode.py [[path]project]

	Examples:
		python pyNewCode.py C:\Users\user\Desktop\MyProject
		(will build MyProject in the C:\Users\user\Desktop directory)
```
In either case, path and project are optional.

If not specified, the current directory and the project name, "myProject" will be used.

If the directory is not specified (a single word given), the current directory will be used.

If the project name is not specified (a path with a trailing path separator is the only option given), then "MyProject" will be used.

---
