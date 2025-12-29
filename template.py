print("Welcome to the Project Scaffold Generator!")
import os, sys
from pathlib import Path
import logging

while True:
    project_name = input("Enter the project name: ").strip()
    if project_name:
        break

#src/__init__.py
#src/components/__init__.py
#src/config/__init__.py
#src/entity/__init__.py
#src/exceptions/__init__.py
#src/logger/__init__.py
#src/pipeline/__init__.py
#src/utils/__init__.py
list_of_files = [
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/exceptions/__init__.py",
    f"src/{project_name}/logger/__init__.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"config/config.yaml",
    "schema.yaml",
    "app.py",
    "logs.py",
    "exceptions.py",
    "setup.py"
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Created directory: {filedir}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
        logging.info(f"Created file: {filepath}")
    else:
        logging.info(f"File already exists and is not empty: {filepath}")