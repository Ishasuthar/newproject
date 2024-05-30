from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT='-e .'

def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n"," ")for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)


    return requirements


setup(
name='BMI prediction using facial images',
version='0.0.1',
author='Isha',
author_email='ishasuthar@gmail.com',
packages=find_packages(),
install_reqires=get_requirements('requirements.txt')
)