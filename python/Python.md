# Python Installation

## 1. Check Python Installation

```command
python3 --version
pip3 --version
```

If not installed, download the latest stable version from [python.org](https://www.python.org)

## 2. Create and Enter the Project Directory

```command
mkdir my_python_project
cd my_python_project
```

## 3. Set Up a Virtual Environment

Create an isolated environment so your project's packages don't interfere with system-wide packages or other projects:

```command
# Create the environment named '.venv'
python3 -m venv .venv

# Activate it on macOS/Linux:
source .venv/bin/activate

# Activate it on Windows (Command Prompt):
source .venv\Scripts\activate.bat

# Activate it on Windows (Git Bash)
source .venv/Scripts/activate

# Activate it on Windows (PowerShell):
source .venv\Scripts\Activate.ps1
```

Once activated, your terminal prompt will show (.venv) at the start.

## 4. Initialize Version Control

```command
git init
```

Create a .gitignore file in your root folder and add the virtual environment directory:

```Plaintext
.venv/
__pycache__/
*.pyc
.env
```

## 5. Create the Recommended Folder Structure

Organize your project into source code, testing, and documentation files:

```Plaintext
my_python_project/
├── .venv/               # Virtual environment (ignored by Git)
├── src/                 # Main application package
│   └── my_project/
│       ├── __init__.py  # Marks directory as a Python package
│       └── main.py      # Entry point
├── tests/               # Test cases
│   └── test_main.py
├── .gitignore           # Git ignore rules
├── README.md            # Project description
└── requirements.txt     # List of project dependencies
```

## 6. Manage Dependencies

Install any required packages (for example, requests) while your virtual environment is active:

```command
pip install requests
```

Save your dependencies to requirements.txt so others can replicate your setup:

```command
pip freeze > requirements.txt
```

(To install dependencies on a new machine later, anyone can run pip install -r requirements.txt).

## 7. Run Your Application

Add a basic print statement inside src/my_project/main.py:

```python
def main():
    print("Hello, Python Project!")

if __name__ == "__main__":
    main()
```

Execute it from the command line:

```command
python src/my_project/main.py
```
