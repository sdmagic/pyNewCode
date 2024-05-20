# pyNewCode

# <p style="text-align: center;">pyNewCode</p>

---

## Description:

This application preforms all the usual tasks of a new project. It:

- Creates a project directory (if we're not using the current directory)
- Creates a modules directory (for python modules and utilities)
  - The modules directory will be a subdirectory off the project directory

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
