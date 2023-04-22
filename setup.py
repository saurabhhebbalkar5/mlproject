from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT ="=e ."
def get_requirements(file_path:str) -> List[str]:
    '''
    This Function will get he package names from requirements.txt file and returns them in a list
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]
    
    if HYPHEN_E_DOT in requirements:
        requirements.remove(HYPHEN_E_DOT)

    return requirements

setup(
    name="mlproject",
    version="0.0.1",
    author="Saurabh Hebbalkar",
    author_email="saurabhhebbalkar@gmail.com",
    packages=find_packages(),
    install_requirements=get_requirements('requirements.txt')
)