<img src="img/logo.png" height="128">

# Python Project Template
A project.

<img src="img/utat-logo.png" height="64">

# Contribution
Instructions for contributing to this project are shown here.
## Setup ⚙️
This section will take you through the procedure to take your development environment from zero to hero.
1. Install python from the official [website](https://www.python.org/downloads/).

    The project runs on python `3.10`.

1. Install [git](https://git-scm.com/).

1. Install [poetry](https://python-poetry.org/).

    The project uses poetry as its package manager. Poetry allows you to run a single command to install all the dependencies for the project. Install it through the Windows Powershell via:
    ```
    (Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | python -
    ```

    On Linux/MacOS with:
    ```
    curl -sSL https://install.python-poetry.org | python3 -
    ```

    Once poetry is installed, if it does not say it has automatically add itself to your PATH, add its executible directory to your PATH:

    Windows: `%APPDATA%\Python\Scripts`

    Linux/MacOS: `$HOME/.local/bin`
    
    For instructions on adding directories to your machine's PATH, check out [this](https://helpdeskgeek.com/windows-10/add-windows-path-environment-variable/) (Windows) or [this](https://stackoverflow.com/a/19663996) (Linux/MacOS). You'll need to close all instances of your terminals for the PATH changes to take effect. 
    
    Confirm poetry was installed correctly by typing the following in your terminal:
    ```
    poetry --version
    ```

    Configure poetry to create its virtual environments within the project's directory. This makes it easier to clean your machine when you delete the project. The `.venv` folders can get pretty big.
    ```
    poetry config virtualenvs.in-project true
    ```

1. Clone the repository.

    It is recommended that you use [Github Desktop](https://desktop.github.com/) to clone the project repository.

1. Install project dependencies

    From a terminal within the cloned repository, run poetry's install command:
    ```
    poetry install
    ```

1. Install recommended extensions for VSCode
    Install the recomended extensions by opening the command pallet using `CMD + shift + P`. Type `Show Reccomended Extensions` and install the extensions listed.

1. Configure IDE interpreter

    It is recommended you use [VSCode](https://code.visualstudio.com/) as your integrated development environment (IDE). Configure your IDE to use the virtual environment poetry has created at `C:\Users\<USERNAME>\AppData\Local\pypoetry\Cache\virtualenvs` (you can also find it with the command `poetry show -v`).
    
    In the case of VSCode, enter the command pallet by going to `View>Command Palette` and search for `Python:Select Interpreter`. Select the appropriate poetry virtual environment for the repository. Restart VSCode if you do not see it listed. Once the intepreter is changed, restart your terminal by closing the old one and launching it again.

    For Windows Powershell users, you might need to change the PS execution policy to allow the script to run. Run a Powershell terminal as administrator and run the following:
    ```
    Set-ExecutionPolicy -ExecutionPolicy Bypass
    ```

1. Install pre-commit hooks

    Install the project's pre-commit hooks using:
    ```
    pre-commit install --install-hooks
    ```
    
    Pre-commit's cache will be stored at `~/.cache/pre-commit` (this folder can grow very large).


You're now ready to start contributing!

## Adding Packages 📦
To add a new package to the poetry virtual environment, install it via:
```
poetry add <package>
```
This is poetry's version of `pip install <package>`.

## Pre-Commit ✅
This project is configured to use [pre-commit](https://pre-commit.com/) hooks. A hook is a script that performs some operation on the repository before every commit. Hooks are used to autoformat and lint code. Pre-commit will not let you push your commit until all hooks pass. When a hook fails, they can be run manually to delint using:
```
pre-commit run --all-files
```

Hooks can be updated using:
```
pre-commit autoupdate
```

## Branches 🌿
Branches are organized as follow:

1. `main`: the branch containing the most recent working release. All code in this branch should run perfectly without any known errors.

1. `dev`: branched off of `main`; the most updated version of the project with the newest features and bug fixes.

1. `<feature>`: branched off of `dev`; a feature branch. Features must be tested thoroughly before being merged into dev.

## Taking on Tickets 🎫
Check out the issues tab to see all open tickets.

## Upgrading Python Version ⬆️
When the project changes python version, it is neccesary to create a new poetry environment with the updated python installation. To do so, proceed as follows:

1. Download and install the required python version from the official website.

1. Within the current poetry environment, call:
    ```
    poetry env use /full/path/to/new/python.exe
    ```
    You can get this path from your environment variables. Poetry will then generate a new empty environment assigned to run using the new python version.

1. Switch to the new empty environment and call:
    ```
    poetry install
    ```
    and
    ```
    pre-commit install --install-hooks
    ```
    To install all the dependencies within this new environment.

You're now ready to start development with the new version of python!



