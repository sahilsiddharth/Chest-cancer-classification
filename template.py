import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s')

project_name="Chest-Cancer-Classification"

list_of_files=[
    ".github/workflows/.gitkeep/",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "templates/index.html",
    "research/trails.ipynb"

]

for filePath in list_of_files:
    filePath=Path(filePath)
    file_dir,file_name=os.path.split(filePath)
    print(file_dir)
    if file_dir !="":
        os.makedirs(file_dir, exist_ok=True)
        logging.info(f"Creating directory : {file_dir} for file : {file_name}")
    if (not os.path.exists(filePath) or (os.path.getsize(filePath) == 0)):
        with open(filePath , "w") as f:
            pass
            logging.info(f"Creating empty file : {filePath} ")
    else:
        logging.info(f"File {filePath} already exists")

