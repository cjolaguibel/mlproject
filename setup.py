# Initial setup script for a machine learning project
from setuptools import find_packages, setup

#function to read the requirements from a file
from typing import List

HYPEN_E_DOT= '-e .'
def get_requirements(file_path: str) -> List[str]:
    """
    Reads the requirements from a file and returns a list of packages.
    """
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements
    
setup(
    name='mlproject',
    version='0.0.1',
    author='Carlos de Olaguibel',
    author_email='carlos.de.olaguibel@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)