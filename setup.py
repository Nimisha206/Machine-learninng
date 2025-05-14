from setuptools import setup, find_packages
from pathlib import Path
from typing import List


def get_requirements(file_path: str) -> List[str]:
    """
    This function reads a requirements file and returns a list of packages.
    :param file_path: str: Path to the requirements file
    :return: list: List of packages
    """
    requirements=[]
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements=[req.replace('\n', '') for req in requirements]
        
        if '-e .' in requirements:
            requirements.remove('-e .')
    return requirements
        

setup(
    name='mlproject',
    version='0.1.0',
    author='Nimisha',
    author_email='tiwarinimisha206@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
    )